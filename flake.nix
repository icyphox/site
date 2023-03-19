{
  description = "site";

  inputs = {
    vite.url = "github:icyphox/go-vite";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, vite }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          devShell = pkgs.mkShell {
            buildInputs = [
              vite.packages.${system}.default
              pkgs.go
              pkgs.gotools
              pkgs.gnumake
              pkgs.entr
            ];
          };
        }
      );

}
