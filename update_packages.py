import json
import os

packages = [
    {
        "schema_version": 1,
        "id": "wine-src",
        "name": "Wine",
        "version": "9.0",
        "type": "source",
        "description": "Compatibility layer capable of running Windows applications",
        "homepage": "https://www.winehq.org",
        "source": {
            "type": "git",
            "url": "https://gitlab.winehq.org/wine/wine.git",
            "ref": "wine-9.0"
        },
        "build": {
            "steps": [
                "./configure",
                "make"
            ]
        },
        "executables": [
            "wine",
            "wine64"
        ]
    },
    {
        "schema_version": 1,
        "id": "neovim-bin",
        "name": "neovim",
        "version": "0.10.0",
        "type": "binary",
        "description": "Vim-fork focused on extensibility and usability",
        "homepage": "https://neovim.io",
        "downloads": {
            "linux-x86_64": {
                "url": "https://github.com/neovim/neovim/releases/download/v0.10.0/nvim-linux64.tar.gz",
                "sha256": "e2e859b819f7a739f50e82ecad8f0d8ef0a324685ff8e75db74384a515f483bf"
            }
        },
        "supported_platforms": [
            "linux-x86_64"
        ]
    },
    {
        "schema_version": 1,
        "id": "neovim-src",
        "name": "neovim",
        "version": "0.10.0",
        "type": "source",
        "description": "Vim-fork focused on extensibility and usability (source build)",
        "homepage": "https://neovim.io",
        "source": {
            "type": "git",
            "url": "https://github.com/neovim/neovim.git",
            "ref": "v0.10.0"
        },
        "build": {
            "system": "cmake"
        },
        "executables": [
            "nvim"
        ]
    },
    {
        "schema_version": 1,
        "id": "helix-bin",
        "name": "helix",
        "version": "25.01",
        "type": "binary",
        "description": "A post-modern modal text editor",
        "homepage": "https://helix-editor.com",
        "downloads": {
            "linux-x86_64": {
                "url": "https://github.com/helix-editor/helix/releases/download/25.01/helix-25.01-x86_64-linux.tar.xz",
                "sha256": "9a0a19fa62243e80ff31237c093a54b38bf213d2a7c49b4c09d5dd2bb67104d4"
            }
        },
        "supported_platforms": [
            "linux-x86_64"
        ]
    },
    {
        "schema_version": 1,
        "id": "helix-src",
        "name": "helix",
        "version": "25.01",
        "type": "source",
        "description": "A post-modern modal text editor (source build)",
        "homepage": "https://helix-editor.com",
        "source": {
            "type": "git",
            "url": "https://github.com/helix-editor/helix.git",
            "ref": "25.01"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "hx"
        ]
    },
    {
        "schema_version": 1,
        "id": "micro-bin",
        "name": "micro",
        "version": "2.0.14",
        "type": "binary",
        "description": "A modern and intuitive terminal-based text editor",
        "homepage": "https://micro-editor.github.io",
        "downloads": {
            "linux-x86_64": {
                "url": "https://github.com/zyedidia/micro/releases/download/v2.0.14/micro-2.0.14-linux64.tar.gz",
                "sha256": "b06385cfd280b1e16c90dddc00fbef73024508ecf66455110d19642e12815340"
            }
        },
        "supported_platforms": [
            "linux-x86_64"
        ]
    },
    {
        "schema_version": 1,
        "id": "ripgrep-src",
        "name": "ripgrep",
        "version": "15.2.0",
        "type": "source",
        "description": "Fast line-oriented search tool that recursively searches directories for a regex pattern (source build)",
        "homepage": "https://github.com/BurntSushi/ripgrep",
        "source": {
            "type": "git",
            "url": "https://github.com/BurntSushi/ripgrep.git",
            "ref": "15.2.0"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "rg"
        ]
    },
    {
        "schema_version": 1,
        "id": "bat-src",
        "name": "bat",
        "version": "0.25.0",
        "type": "source",
        "description": "A cat(1) clone with syntax highlighting and Git integration (source build)",
        "homepage": "https://github.com/sharkdp/bat",
        "source": {
            "type": "git",
            "url": "https://github.com/sharkdp/bat.git",
            "ref": "v0.25.0"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "bat"
        ]
    },
    {
        "schema_version": 1,
        "id": "btop-src",
        "name": "btop",
        "version": "1.4.0",
        "type": "source",
        "description": "A monitor of resources (CPU, memory, disks, network and processes) (source build)",
        "homepage": "https://github.com/aristocratos/btop",
        "source": {
            "type": "git",
            "url": "https://github.com/aristocratos/btop.git",
            "ref": "v1.4.0"
        },
        "build": {
            "system": "make"
        },
        "executables": [
            "btop"
        ]
    },
    {
        "schema_version": 1,
        "id": "fzf-src",
        "name": "fzf",
        "version": "0.60.3",
        "type": "source",
        "description": "A general-purpose command-line fuzzy finder (source build)",
        "homepage": "https://github.com/junegunn/fzf",
        "source": {
            "type": "git",
            "url": "https://github.com/junegunn/fzf.git",
            "ref": "v0.60.3"
        },
        "build": {
            "steps": [
                "go build -v -o fzf"
            ]
        },
        "executables": [
            "fzf"
        ]
    },
    {
        "schema_version": 1,
        "id": "duf-src",
        "name": "duf",
        "version": "0.8.0",
        "type": "source",
        "description": "Disk Usage/Free Utility - a better 'df' alternative (source build)",
        "homepage": "https://github.com/muesli/duf",
        "source": {
            "type": "git",
            "url": "https://github.com/muesli/duf.git",
            "ref": "v0.8.0"
        },
        "build": {
            "steps": [
                "go build -v -o duf"
            ]
        },
        "executables": [
            "duf"
        ]
    },
    {
        "schema_version": 1,
        "id": "dust-src",
        "name": "dust",
        "version": "1.1.2",
        "type": "source",
        "description": "A more intuitive version of du in rust (source build)",
        "homepage": "https://github.com/bootandy/dust",
        "source": {
            "type": "git",
            "url": "https://github.com/bootandy/dust.git",
            "ref": "v1.1.2"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "dust"
        ]
    },
    {
        "schema_version": 1,
        "id": "lazygit-src",
        "name": "lazygit",
        "version": "0.48.0",
        "type": "source",
        "description": "Simple terminal UI for git commands (source build)",
        "homepage": "https://github.com/jesseduffield/lazygit",
        "source": {
            "type": "git",
            "url": "https://github.com/jesseduffield/lazygit.git",
            "ref": "v0.48.0"
        },
        "build": {
            "steps": [
                "go build -v -o lazygit"
            ]
        },
        "executables": [
            "lazygit"
        ]
    },
    {
        "schema_version": 1,
        "id": "hyperfine-src",
        "name": "hyperfine",
        "version": "1.19.0",
        "type": "source",
        "description": "A command-line benchmarking tool (source build)",
        "homepage": "https://github.com/sharkdp/hyperfine",
        "source": {
            "type": "git",
            "url": "https://github.com/sharkdp/hyperfine.git",
            "ref": "v1.19.0"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "hyperfine"
        ]
    },
    {
        "schema_version": 1,
        "id": "tokei-src",
        "name": "tokei",
        "version": "12.1.2",
        "type": "source",
        "description": "A program that displays statistics about your code (source build)",
        "homepage": "https://github.com/Xaeroxe/tokei",
        "source": {
            "type": "git",
            "url": "https://github.com/Xaeroxe/tokei.git",
            "ref": "v12.1.2"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "tokei"
        ]
    },
    {
        "schema_version": 1,
        "id": "starship-src",
        "name": "starship",
        "version": "1.22.1",
        "type": "source",
        "description": "The minimal, blazing-fast, and infinitely customizable prompt for any shell (source build)",
        "homepage": "https://starship.rs",
        "source": {
            "type": "git",
            "url": "https://github.com/starship/starship.git",
            "ref": "v1.22.1"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "starship"
        ]
    },
    {
        "schema_version": 1,
        "id": "gh-src",
        "name": "gh",
        "version": "2.68.0",
        "type": "source",
        "description": "GitHub's official command line tool (source build)",
        "homepage": "https://github.com/cli/cli",
        "source": {
            "type": "git",
            "url": "https://github.com/cli/cli.git",
            "ref": "v2.68.0"
        },
        "build": {
            "steps": [
                "go build -v -o gh ./cmd/gh"
            ]
        },
        "executables": [
            "gh"
        ]
    },
    {
        "schema_version": 1,
        "id": "just-src",
        "name": "just",
        "version": "1.39.0",
        "type": "source",
        "description": "Just a command runner (source build)",
        "homepage": "https://github.com/casey/just",
        "source": {
            "type": "git",
            "url": "https://github.com/casey/just.git",
            "ref": "1.39.0"
        },
        "build": {
            "system": "cargo",
            "release": True,
            "locked": True
        },
        "executables": [
            "just"
        ]
    },
    {
        "schema_version": 1,
        "id": "fish-src",
        "name": "fish",
        "version": "3.7.1",
        "type": "source",
        "description": "Smart and user-friendly command line shell",
        "homepage": "https://fishshell.com",
        "source": {
            "type": "git",
            "url": "https://github.com/fish-shell/fish-shell.git",
            "ref": "3.7.1"
        },
        "build": {
            "system": "cmake"
        },
        "executables": [
            "fish"
        ]
    },
    {
        "schema_version": 1,
        "id": "curl-src",
        "name": "curl",
        "version": "8.12.1",
        "type": "source",
        "description": "Command line tool and library for transferring data with URLs",
        "homepage": "https://curl.se",
        "source": {
            "type": "git",
            "url": "https://github.com/curl/curl.git",
            "ref": "curl-8_12_1"
        },
        "build": {
            "steps": [
                "./autoreconf -fi",
                "./configure",
                "make"
            ]
        },
        "executables": [
            "curl"
        ]
    },
    {
        "schema_version": 1,
        "id": "wget-src",
        "name": "wget",
        "version": "1.25.0",
        "type": "source",
        "description": "Tool for retrieving files using HTTP, HTTPS, and FTP",
        "homepage": "https://www.gnu.org/software/wget/",
        "source": {
            "type": "git",
            "url": "https://git.savannah.gnu.org/git/wget.git",
            "ref": "v1.25.0"
        },
        "build": {
            "steps": [
                "./bootstrap",
                "./configure",
                "make"
            ]
        },
        "executables": [
            "wget"
        ]
    }
]

def main():
    with open("index.json", "r") as f:
        index_data = json.load(f)

    for pkg in packages:
        pkg_id = pkg["id"]
        def_path = f"packages/{pkg_id}.json"

        # Write individual package json
        with open(def_path, "w") as f:
            json.dump(pkg, f, indent=4)
            f.write("\n")

        # Update index.json
        index_data["packages"][pkg_id] = {
            "definition": def_path,
            "type": pkg["type"],
            "description": pkg["description"]
        }

    with open("index.json", "w") as f:
        json.dump(index_data, f, indent=4)
        f.write("\n")

    print(f"Successfully created {len(packages)} packages and updated index.json")

if __name__ == "__main__":
    main()
