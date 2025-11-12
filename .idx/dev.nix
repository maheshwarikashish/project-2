{ pkgs, ... }: {
  # Nix channel to use.
  channel = "stable-24.05";

  # Packages to make available in the environment.
  packages = [
    # For Module 4: Frontend
    pkgs.nodejs_20

    # For Modules 1, 2, 3: Python Backend
    (pkgs.python3.withPackages (ps: [
      ps.pip
      ps.requests
      ps.beautifulsoup4
      ps.pandas
      ps.flask
    ]))
  ];

  # Environment variables to set.
  env = {};

  # VS Code extensions to install.
  idx.extensions = [
    "ms-python.python"
    "dbaeumer.vscode-eslint" # For frontend development
  ];

  # Workspace lifecycle hooks.
  idx.workspace = {
    # Runs when a workspace is first created.
    onCreate = {
      # Example: install dependencies
      # install-deps = "npm install";
    };
    # Runs every time the workspace is (re)started.
    onStart = {
      # Example: start a dev server
      # start-server = "npm run dev";
    };
  };
}
