{
  description = "site";

  inputs.nixpkgs.url = "github:nixos/nixpkgs";
  inputs.vite.url = "github:icyphox/go-vite";

  outputs =
    { self
    , nixpkgs
    , vite
    ,
    }:
    let
      supportedSystems = [
        "x86_64-linux"
        "x86_64-darwin"
        "aarch64-linux"
        "aarch64-darwin"
      ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; });
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        {
          default = pkgs.mkShell {
            buildInputs = [
              vite.packages.${system}.vite
              pkgs.gotools
              pkgs.gnumake
              pkgs.entr
              pkgs.awscli2
            ];
          };
        }
      );

      apps = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        {
          default = {
            type = "app";
            program = "${pkgs.writeShellScriptBin "vite-build" ''
              #!/usr/bin/env bash
              ${vite.packages.${system}.vite}/bin/vite build
            ''}/bin/vite-build";
            cwd = ./.;
          };
          deploy = {
            type = "app";
            program = "${pkgs.writeShellScriptBin "s3-sync" ''
                #!/usr/bin/env bash
                ${vite.packages.${system}.vite}/bin/vite build
                ${pkgs.awscli2}/bin/aws s3 sync build s3://site/ --size-only
            ''}/bin/s3-sync";
          };
        }
      );
    };
}
