{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.wheel
    pkgs.gcc
    pkgs.rustc
    pkgs.cargo
    pkgs.nodePackages.npm
    pkgs.nodejs
  ];
}
