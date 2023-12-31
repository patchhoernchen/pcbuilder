# PC builder toy

This is just a hacky toy to build a new PC. From a set of components several
builds can be derived. The costs per build are calculated and shown along with
an overview. Alternatively a link list can be generated or opened.

Don't expect to much. Especially documentation. This is [klingon
software](https://www.mikrocontroller.net/topic/1675). If it bites you, it's
entirely your fault ;)

## usage

```
./pc.py --help
usage: PC Builder [-h] [-B buildsfile] [-C componentsfile] [-l] [-L] [-w webbrowser] build

build different pc combinations from a set of components

positional arguments:
  build                 use this specific build, use 'all' for all builds

options:
  -h, --help            show this help message and exit
  -B buildsfile, --buildsfile buildsfile
                        file containing builds
  -C componentsfile, --componentsfile componentsfile
                        file containing parts
  -l, --links           open links for build
  -L, --show-links      show links for build
  -w webbrowser, --webbrowser webbrowser
                        open link for build

-l and -L only work when a build is specified
```

## output

```
./pc.py FAV
FAV: 1661.38 Euro
1x AMD Ryzen 8 7800X3D (393.99€ pp) - https://geizhals.de/amd-ryzen-7-7800x3d-100-100000910wof-a2872148.html
1x SAPPHIRE Radeon RX 7800XT 16GB (547.99€ pp) - https://geizhals.de/sapphire-radeon-rx-7800-xt-v139043.html
1x MSI MAG B650 Tomahawk WIFI (207.0€ pp) - https://geizhals.de/msi-mag-b650-tomahawk-wifi-a2824300.html
1x G.Skill Flare X5 schwarz DIMM Kit 32GB, DDR5-6000, CL32-38-38-96, on-die ECC (118.33€ pp) - https://geizhals.de/g-skill-flare-x5-schwarz-dimm-kit-32gb-f5-6000j3238f16gx2-fx5-a2816010.html
2x TEAMGROUP MP33 SSD 1TB M.2 (47.43€ pp) - https://geizhals.de/?fs=TEAMGROUP+MP33+SSD+1TB+M.2&hloc=at&hloc=de
1x 850 Watt be quiet! System Power 10 Non-Modular 80+ Gold (97.32€ pp) - https://www.mindfactory.de/product_info.php/850-Watt-be-quiet--System-Power-10-Non-Modular-80--Gold_1470342.html
1x be quiet! Dark Rock 4 (80€ pp) - https://geizhals.de/be-quiet-dark-rock-4-v50714.html
1x Fractal Design North Black (121.89€ pp) - https://geizhals.de/fractal-design-north-v119325.html
```

## License

WTFPL

## Contact

patchhoernchen+git (mailboxseperator) unavailable (domainlabelseperator) network
