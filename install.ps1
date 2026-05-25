# Install Web3 Product Manager skills into Cursor (Windows).
param(
    [Parameter(Position = 0)]
    [string]$Target = "",
    [switch]$Personal
)

$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot
$SkillsSrc = Join-Path $RepoRoot "skills"
$ExamplesSrc = Join-Path $RepoRoot "examples"

function Get-DestRoot {
    if ($Personal) {
        return Join-Path $env:USERPROFILE ".cursor\skills"
    }
    if (-not $Target) {
        throw "Provide -Target <project-path> or -Personal"
    }
    $resolved = Resolve-Path $Target
    return Join-Path $resolved ".cursor\skills"
}

function Copy-Examples([string]$Dest) {
    $exDest = Join-Path $Dest "examples"
    if (-not (Test-Path $ExamplesSrc)) { return }
    New-Item -ItemType Directory -Force -Path $exDest | Out-Null
    Copy-Item -Path (Join-Path $ExamplesSrc "*") -Destination $exDest -Recurse -Force
}

function Install-Skill([string]$SkillDir, [string]$DestRoot) {
    $name = Split-Path $SkillDir -Leaf
    $dest = Join-Path $DestRoot $name
    if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item (Join-Path $SkillDir "SKILL.md") $dest
    $refs = Join-Path $SkillDir "references"
    if (Test-Path $refs) {
        Copy-Item $refs (Join-Path $dest "references") -Recurse
    }
    Copy-Examples $dest
    Write-Host "Installed: $dest"
}

$destRoot = Get-DestRoot
New-Item -ItemType Directory -Force -Path $destRoot | Out-Null
$count = 0
Get-ChildItem $SkillsSrc -Directory | ForEach-Object {
    if (Test-Path (Join-Path $_.FullName "SKILL.md")) {
        Install-Skill $_.FullName $destRoot
        $count++
    }
}
if ($count -eq 0) { throw "No skills found under $SkillsSrc" }
Write-Host "Done. $count skill(s) -> $destRoot"
Write-Host "Reload Cursor. Invoke: /web3-product-manager"
