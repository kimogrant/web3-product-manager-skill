#!/usr/bin/env bash
# Install Web3 Product Manager skills into Cursor skill directories.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="${REPO_ROOT}/skills"

usage() {
  cat <<'EOF'
Usage:
  ./skill.sh list
  ./skill.sh install <target-project-path>
  ./skill.sh install --personal

Copies each skill bundle (SKILL.md + references/ + examples if present)
into <target>/.cursor/skills/<skill-name>/ or ~/.cursor/skills/<skill-name>/.
EOF
}

list_skills() {
  find "${SKILLS_SRC}" -mindepth 1 -maxdepth 1 -type d | sort | while read -r dir; do
    if [[ -f "${dir}/SKILL.md" ]]; then
      basename "${dir}"
    fi
  done
}

install_one() {
  local skill_dir="$1"
  local dest_root="$2"
  local name
  name="$(basename "${skill_dir}")"
  local dest="${dest_root}/${name}"

  mkdir -p "${dest_root}"
  rm -rf "${dest}"
  mkdir -p "${dest}"
  cp "${skill_dir}/SKILL.md" "${dest}/"
  if [[ -d "${skill_dir}/references" ]]; then
    cp -R "${skill_dir}/references" "${dest}/"
  fi
  if [[ -d "${skill_dir}/examples" ]]; then
    cp -R "${skill_dir}/examples" "${dest}/"
  fi
  echo "Installed: ${dest}"
}

cmd_install() {
  local target="${1:-}"
  local dest_root

  if [[ "${target}" == "--personal" ]]; then
    dest_root="${HOME}/.cursor/skills"
  else
    if [[ -z "${target}" ]]; then
      echo "Error: provide target project path or --personal" >&2
      usage
      exit 1
    fi
    if [[ ! -d "${target}" ]]; then
      echo "Error: target directory does not exist: ${target}" >&2
      exit 1
    fi
    dest_root="$(cd "${target}" && pwd)/.cursor/skills"
  fi

  mkdir -p "${dest_root}"
  local count=0
  while read -r skill_dir; do
    install_one "${skill_dir}" "${dest_root}"
    count=$((count + 1))
  done < <(find "${SKILLS_SRC}" -mindepth 1 -maxdepth 1 -type d | sort)

  if [[ "${count}" -eq 0 ]]; then
    echo "No skills found under ${SKILLS_SRC}" >&2
    exit 1
  fi
  echo "Done. ${count} skill(s) -> ${dest_root}"
  echo "Reload Cursor, then invoke /web3-product-strategy or /web3-product-specification"
}

case "${1:-}" in
  list)
    echo "Skills in this repository:"
    list_skills
    ;;
  install)
    cmd_install "${2:-}"
    ;;
  -h|--help|help|"")
    usage
    ;;
  *)
    echo "Unknown command: ${1}" >&2
    usage
    exit 1
    ;;
esac
