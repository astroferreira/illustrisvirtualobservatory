
#!/usr/bin/env python
"""

                                                       Backup

     Author:  P. Torrey (ptorrey@mit.edu) 1/24/15
     Updated: T. Metivier (tylerphys@uconn.edu) 5/9/18 (with R. Mandelbaum's Github for reference)
"""
print(r"""


 ____________________________________________________________________________________________________________
/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/
  ██╗██╗     ██╗     ██╗  *██╗███████╗████████╗██████╗ ██╗███████╗      *               *               *
  ██║██║ *   ██║     ██║ * ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝                          *
  ██║██║     ██║     ██║   ██║███████╗   ██║ * ██████╔╝██║███████╗*              *
  ██║██║     ██║  *  ██║   ██║╚════██║ * ██║   ██╔══██╗██║╚════██║       *         *            **
  ██║███████╗███████╗╚██████╔╝███████║   ██║   ██║  ██║██║███████║                 \│/  *                   ,-.
  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝          *     - o -        *           / \  `.  __..-,O
██╗*  ██╗██╗██████╗ ████████╗██╗ * ██╗ █████╗ ██╗    *                *            /│\                *   :   \ --''_..-'.'
██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║                 *         *             *               |    . .-' `. '.
██║ * ██║██║██████╔╝   ██║   ██║   ██║███████║██║    *       *                    *                       :     .     .`.'
╚██╗ ██╔╝██║██╔══██╗ * ██║   ██║   ██║██╔══██║██║                          *                               \     `.  /  ..
 ╚████╔╝ ██║██║  ██║   ██║  *╚██████╔╝██║  ██║███████╗       *                       *         *        *   \      `.   ' .
  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝                   *                                   `,       `.   \
    *    ██████╗ ██████╗ ███████╗███████╗██████╗ ██╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ ██╗   ██╗       ,|,`.        `-.\
        ██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝      '.||  ``-...__..-`
*       ██║   ██║██████╔╝███████╗█████╗  ██████╔╝██║   ██║███████║   ██║   ██║   ██║██████╔╝ ╚████╔╝        |  |
        ██║   ██║██╔══██╗╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝         |__|
*       ╚██████╔╝██████╔╝███████║███████╗██║  ██║ ╚████╔╝ ██║  ██║   ██║   ╚██████╔╝██║  ██║   ██║          /||\
                            *                        *                  *                                  //||\\
*         **       *                    *                           *           *           *             // || \\
    *                *          *                    *     *                         *                 __//__||__\\__
        *        *               *            *                   *               *              *    '--------------'
 ____________________________________________________________________________________________________________
/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/

""")
start = input(r"""

       \│/           ┌─┐┬─┐┌─┐┌─┐┌─┐  ╔═╗╔╗╔╔╦╗╔═╗╦═╗  ┌┬┐┌─┐  ┌─┐┌─┐┌┐┌┌┬┐┬┌┐┌┬ ┬┌─┐           \│/
       ─ ──────────  ├─┘├┬┘├┤ └─┐└─┐  ║╣ ║║║ ║ ║╣ ╠╦╝   │ │ │  │  │ ││││ │ │││││ │├┤   ────────── ─
       /│\           ┴  ┴└─└─┘└─┘└─┘  ╚═╝╝╚╝ ╩ ╚═╝╩╚═   ┴ └─┘  └─┘└─┘┘└┘ ┴ ┴┘└┘└─┘└─┘           /│\

""")

import numpy as np
import os
import sys
sys.path.append('../..')
import sunpy__load as sunpy__load
import sunpy__plot as sunpy__plot

pal = input(r'''
____________________________________________________________________________________________________________________


                                                Hello!
                                           What is your name?

____________________________________________________________________________________________________________________

                                             : ''')

print('''
____________________________________________________________________________________________________________________

                                     It`s nice to meet you,''', pal)

my_api = "a4385a1f5eac5c06e2e2c1f45eebb4d3"
dl_base = 'http://www.illustris-project.org'

try:
    # Depending on the NumPy version, the line below can raise a TypeError even if the file is
    # present.  The try/except block enables us to try loadtxt calls that work for more NumPy
    # versions.
    try:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i10', 'f8')})
    except TypeError:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i8', 'f8')})
except IOError:
    # If we don't already have the file, we have to download it and try again.
    os.system("wget " + dl_base + "/files/directory_catalog_135.txt")
    try:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i10', 'f8')})
    except TypeError:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i8', 'f8')})
all_subdirs = catalog['subdirs']
all_galnrs = catalog['galaxy_numbers']


common_args = {
    # default option = False, turn on one-by-one
    'add_background':       False,
    'add_noise':            True,
    'add_psf':              True,
    'rebin_phys':           True,
    'resize_rp':            False,
    'rebin_gz':             True,           # always true, all pngs 424x424
    'scale_min':            1e-10,          # was 1e-4
    'lupton_alpha':         2e-12,          # was 1e-4
    'lupton_Q':             10,             # was ~100
    'pixelsize_arcsec':     0.06,           # SDSS - 0.24
    'psf_fwhm_arcsec':      0.13,            # SDSS - 1.0
    # super low noise value, dominated by background
    'sn_limit':             25.0,
    'sky_sig':              None,           #
    'redshift':             0.01,           #
    'b_fac':                1.1,
    'g_fac':                1.0,
    'r_fac':                0.9,
    'camera':               1,
    'seed_boost':           1.0,
    'save_fits':            True
}


for index, galnr in enumerate(all_galnrs[:1]):
    galnr = input('''
____________________________________________________________________________________________________________________


                                    Please enter the galaxy ID number: ''')
    print("You chose galaxy", galnr)
    cmd = 'wget --content-disposition --header="API-Key: ' + my_api + '" "' + dl_base + \
        '/api/Illustris-1/snapshots/135/subhalos/' + str(galnr) +  \
        '/stellar_mocks/broadband.fits"'

    if(not (os.path.isfile("./broadband_" + str(galnr) + ".fits"))):
        os.system(cmd)
    filename = "./broadband_" + str(galnr) + ".fits"

tele = input('''
____________________________________________________________________________________________________________________


                              ┌─┐┌─┐┬  ┌─┐┌─┐┌┬┐  ┌─┐┌┐┌  ┬┌┐┌┌─┐┌┬┐┬─┐┬ ┬┌┬┐┌─┐┌┐┌┌┬┐
            ──────────────────└─┐├┤ │  ├┤ │   │   ├─┤│││  ││││└─┐ │ ├┬┘│ ││││├┤ │││ │──────────────────
                              └─┘└─┘┴─┘└─┘└─┘ ┴   ┴ ┴┘└┘  ┴┘└┘└─┘ ┴ ┴└─└─┘┴ ┴└─┘┘└┘ ┴

                Hubble Space Telescope (1)          or            Sloan Digital Sky Survey (2)


                                             (enter '1' or '2')
                                                     :''')
if tele == '2':
    common_args['pixelsize_arcsec'] = 0.24
    common_args['psf_fwhm_arcsec'] = 1.0
    sunpy__plot.plot_synthetic_sdss_gri(
        filename, savefile='./synthetic_sdss_gri_' + str(galnr) + '.png', **common_args)
    print('Your Sloan Digital Sky Survey Observations are complete,', pal)

elif tele == '1':
    sunpy__plot.plot_synthetic_hst(
        filename, savefile='./synthetic_hst' + str(galnr) + '.png', **common_args)
    print('Your Hubble Space Telescope Observations are complete,', pal)

else:
    print('I do not understand what you mean', pal)

input(r'''
____________________________________________________________________________________________________________________
                                 ______                      __     __
                                / ____/___  ____ ___  ____  / /__  / /____
                               / /   / __ \/ __ `__ \/ __ \/ / _ \/ __/ _ \
                              / /___/ /_/ / / / / / / /_/ / /  __/ /_/  __/
                              \____/\____/_/ /_/ /_/ .___/_/\___/\__/\___/
                                                  /_/
____________________________________________________________________________________________________________________
                                                --(Press enter to end program)--
''')
input(r"""
                               ╦ ╦╔═╗┌─┐┌┐┌┌┐┌  ╔═╗┌─┐┌┬┐┬─┐┌─┐┌─┐┬ ┬┬ ┬┌─┐┬┌─┐┌─┐
                               ║ ║║  │ │││││││  ╠═╣└─┐ │ ├┬┘│ │├─┘├─┤└┬┘└─┐││  └─┐
                               ╚═╝╚═╝└─┘┘└┘┘└┘  ╩ ╩└─┘ ┴ ┴└─└─┘┴  ┴ ┴ ┴ └─┘┴└─┘└─┘
                        ╦ ╦┬ ┬┬┌┬┐┌─┐┬┌─┌─┐┬─┐  ╦═╗┌─┐┌─┐┌─┐┌─┐┬─┐┌─┐┬ ┬  ╔═╗┬─┐┌─┐┬ ┬┌─┐
                        ║║║├─┤│ │ ├─┤├┴┐├┤ ├┬┘  ╠╦╝├┤ └─┐├┤ ├─┤├┬┘│  ├─┤  ║ ╦├┬┘│ ││ │├─┘
                        ╚╩╝┴ ┴┴ ┴ ┴ ┴┴ ┴└─┘┴└─  ╩╚═└─┘└─┘└─┘┴ ┴┴└─└─┘┴ ┴  ╚═╝┴└─└─┘└─┘┴
                                       ╔╗╔╔═╗╔═╗╔═╗  ╔═╗╔╦╗  ╔═╗ ╔═╗ ╔═╗
                                       ║║║╠═╣╚═╗╠═╣  ║   ║   ╚═╗ ║ ╦ ║
                                       ╝╚╝╩ ╩╚═╝╩ ╩  ╚═╝ ╩   ╚═╝.╚═╝.╚═╝.
                                                    -(enter)-
____________________________________________________________________________________________________________________
""")
print("""


                                              *                                  .,
                                          ,#%%%%%(                            /%%%%%%/
                                       #%%%%,   (%%%%,                    .%%%%#.   #%%%#.
                                   ,%%%%(          ,%%%%(              /%%%%/          *%%%%*
                                #%%%(                  ,%%%%*      .%%%%(          (%%%%%%%%%%%%.
                            ,%%%%(                         #%%%#/%%%%/          #%%%%%%%%%%%%%%%%%%/
                           /%%,                               /%%%.          ,%%%%%%#,        #%  (%#
                           (%#                                 %%/         .%%%%%%  (%%%%%/    .* .%#
                           #%#                                 %%/        (%%%%%  %%%%%%%%%%,   , .%#
                           #%#                                 %%/       #%%%%, .%%%%%%%%%%%%     .%#
                           %%#                                 %%/    / %%%%%   %%%%%%%%%*%%%.    .%#
                           %%#                                 %%/   ,./%%%%    %%%%%%%#,%%%%     .%#
                           %%#                                 %%/   % %%%%/     /%%%, #%%%%*     .%%
                           %%#                                 %%/  #% %%%%/         (%%%%%/      .%%
                           %%#                                 %%/  %% %%%%%#.   .(%%%%%%%,       .%%
                           %%#                                 %%/  %% /%%%%%%%%%%%%%%%%#         .%%.
                         .#%%%(                              ,%%%%* *%% .%%%%%%%%%%%%%*          *%%%%.
                      ,%%%%/,%%%%#.                       /%%%%((%%%%%%%/  (%%%%%%#,          #%%%%/(%%%%*
                   (%%%#.       (%%%%,                .#%%%%,      .#%%%%%#(.             ,%%%%#.      ,%%%%*
               .#%%%#              /%%%%(          *%%%%#.             (%%%%/          /%%%%(             .#%%%#
            *%%%%*                    .#%%%%,  .#%%%%(.                  ./%%%%#.  .#%%%%,                    /%%%%*
         .%%%#.                           (%%%%%%#.%%%%%%%%,          %%%%%%%*#%%%%%%(                           .#%%%/
         .%*                    ./%%%%%%%    %%    #%%%  %%/          %%/ *%%   .%%                                 *%%
         .%*                %%%%%%%%%%%%%*   %%    (%%%/#%%/ (%%%%%%  %%%.%%%   .%%                                 *%%
         .%*          (%%%% %%%%%%%%%%%%%%   %%    ,%%%%%%%//%%%%%%%(,%%%%%%#   .%%                                 *%%
         .%*     ./#.(%%%%% %%%%%%%%%%%%%%,  %%     %%%%%%%%%%*  %%%%#%%%%%%*   .%%                                 *%%
         .%*    %%%%(*%%%%%(,%%%%%%%%%%%%#,  %%     %%%..%%%%%%%%%%%%%%/ *%%.   .%%                                 *%%
         .%*    *%%%%.(%%%%%/.%%%#/.         %%     (%%*(%%%%%%%%%%%%%%%*%%%    .%%                                 *%%
         .%*             *#%%#               %%     ,%%%%%%%%%%%%%%/*/%%%%%#    .%%                                 *%%
         .%*             #%%%#               %%      %%%%%. .%%%%%%# #%%%%%*    .%%                                 *%%
         .%*            %%%%%%#              %%      %%%%%%%%%%..%%%%%%%%%%     .%%                                 *%%
         .%*           %% /%/.%%             %%      #%%%%%%%%,  (%%%%%%%%%     .%%                                 *%%
         .%%%(       .%#  /%/  %%,        /%%%%%%/   /%%  *%%*    %%%%  ,%#   /%%%%%%*                            (%%%*
             (%%%/  (%(   /%/   *%#   *%%%%%,   (%%%%/%%%%%%*      %%%%%%%#%%%%#   .#%%%%,                    (%%%#
                *%%%%/    /%/    .%%%%%%(          ,%%%%%,.           ,%%%%%/%#        *%%%%(             ,%%%%*
                   .#%%%* /%(  .#%%%%,                 (%%%%,      ,%%%%#.  .%%            #%%%#.      *%%%#.
                       #%%%%%%%%%#.                       ,%%%%/(%%%%(   ,#%%%%%%#*           (%%%%/#%%%#
                          (%%%/                              .#%%%*         /%%.                 ,%%%/
                           %%#                                 %%/           %#                   .%%.
                           %%#                                 %%/           (*         .%        .%%
                           %%#                                 %%*           .          %%(       .%%
                           %%#                                 %%*                    .%%%%#      .%%
                           %%#                                 %%*          ,*(#%%%%%%%%%%%%%%%%%%%%#
                           %%#                                 %%*               .*/#%%%%%%%%%(/,.,%#
                           %%#                                 %%*      ((             /%%%,      .%#
                           #%#                                 %%*     /%%/             %%/       .%#
                           (%#                                 %%%%%%%%%%%%%%%%%#/,.    .%        .%#
                           ,%%,                               (%%%.  ./%%%%/                     .#%#
                             #%%%(                        .%%%%(/%%%%/  %%                    ,%%%%.
                                /%%%#                  *%%%#.       #%%%%(                 *%%%(
                                   *%%%%*           (%%%(              /%%%%,          .#%%%/
                                       /%%%%,   (%%%#                      (%%%#.  .#%%%(
                                          ,%%%%%%,                            ,%%%%%%,
                                                                                                    
____________________________________________________________________________________________________________________
""")
# restore_common_args()
