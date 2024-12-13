{
  description = "Python development environment with pytest and tkinter";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          pytest
          tkinter
          # Add any other Python packages you need here
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv
            # Additional development tools
            black    # Python formatter
            ruff     # Fast Python linter
            git
          ];

          shellHook = ''
            echo "Python development environment loaded with pytest and tkinter"
            echo "Python version: $(python --version)"
          '';
        };
      });
}
