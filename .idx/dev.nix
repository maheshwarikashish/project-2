{ pkgs, ... }: {
  # Nix channel to use.
  channel = "stable-24.05";

  # Packages to make available in the environment.
  packages = [
    pkgs.chromium
    pkgs.chromedriver
    (pkgs.python3.withPackages (ps: [
      ps.pip
      ps.requests
      ps.beautifulsoup4
      ps.selenium
    ]))
  ];

  # Environment variables to set.
  env = {};

  # VS Code extensions to install.
  idx.extensions = [
    "ms-python.python"
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

  # Web previews.
  idx.previews = {
    enable = true;
    previews = {
      # web = {
      #   command = ["npm" "run" "dev" "--" "--port" "$PORT"];
      #   manager = "web";
      # };
    };
  };
}
