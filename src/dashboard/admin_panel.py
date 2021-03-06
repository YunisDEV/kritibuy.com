from .admin import admin_data_get, admin_data_post, admin_data_delete, admin_data_update

adminDashboardTree = {
    "analytics": {
        "icon": """
        <svg style="fill:white;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 328.668 328.668" style="enable-background:new 0 0 328.668 328.668;" xml:space="preserve"> <g> <g> <path d="M19.334,216.001h-10c-2.761,0-5,2.239-5,5v74c0,2.761,2.239,5,5,5h10c2.761,0,5-2.239,5-5v-74    C24.334,218.24,22.095,216.001,19.334,216.001z"/> <path d="M79.334,216.001h-10c-2.761,0-5,2.239-5,5v74c0,2.761,2.239,5,5,5h10c2.761,0,5-2.239,5-5v-74    C84.334,218.24,82.095,216.001,79.334,216.001z"/> <path d="M139.334,162.001h-10c-2.761,0-5,2.239-5,5v128c0,2.761,2.239,5,5,5h10c2.761,0,5-2.239,5-5v-128    C144.334,164.24,142.095,162.001,139.334,162.001z"/> <path d="M199.334,120.001h-10c-2.761,0-5,2.239-5,5v170c0,2.761,2.239,5,5,5h10c2.761,0,5-2.239,5-5v-170    C204.334,122.24,202.095,120.001,199.334,120.001z"/> <path d="M259.334,162.001h-10c-2.761,0-5,2.239-5,5v128c0,2.761,2.239,5,5,5h10c2.761,0,5-2.239,5-5v-128    C264.334,164.24,262.095,162.001,259.334,162.001z"/> <path d="M319.334,96.001h-10c-2.761,0-5,2.239-5,5v194c0,2.761,2.239,5,5,5h10c2.761,0,5-2.239,5-5v-194    C324.334,98.24,322.095,96.001,319.334,96.001z"/> </g> <path d="M314.334,28.667c-7.904,0-14.334,6.43-14.334,14.334c0,3.025,0.948,5.83,2.554,8.146l-43.781,62.753   c-1.4-0.457-2.89-0.712-4.439-0.712c-3.394,0-6.51,1.191-8.968,3.169l-37.088-26.785c0.247-1.052,0.39-2.142,0.39-3.268   c0-7.903-6.43-14.333-14.334-14.333S180,78.4,180,86.304c0,1.308,0.191,2.569,0.52,3.773l-40.188,31.257   c-1.828-0.847-3.855-1.333-5.999-1.333c-7.896,0-14.32,6.418-14.333,14.31l-36.188,19.3c-2.53-2.238-5.844-3.61-9.479-3.61   c-5.36,0-10.035,2.961-12.494,7.329l-33.462-5.205c-1.335-6.531-7.125-11.458-14.044-11.458C6.43,140.667,0,147.097,0,155.001   c0,7.903,6.43,14.333,14.334,14.333c5.36,0,10.035-2.961,12.494-7.33l33.462,5.205c1.335,6.531,7.125,11.458,14.044,11.458   c7.904,0,14.334-6.43,14.334-14.334c0-0.646-0.058-1.278-0.142-1.903l35.027-18.681c2.629,3.007,6.481,4.918,10.78,4.918   c7.904,0,14.334-6.43,14.334-14.334c0-2.08-0.455-4.052-1.256-5.838l38.945-30.29c2.282,1.534,5.026,2.432,7.977,2.432   c3.136,0,6.031-1.024,8.394-2.739l37.51,27.09c-0.148,0.824-0.238,1.668-0.238,2.533c0,7.903,6.43,14.333,14.334,14.333   s14.334-6.43,14.334-14.333c0-2.697-0.763-5.213-2.064-7.37l44.154-63.287c1.146,0.296,2.339,0.47,3.576,0.47   c7.904,0,14.334-6.43,14.334-14.333C328.668,35.097,322.238,28.667,314.334,28.667z"/> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> <g> </g> </svg>
        """,
        "indexes": [
            {
                "name": 'Dashboard',
                "url": '/dashboard',
                "icon": 'dripicons-meter'
            },
            {

                "name": 'Wallet',
                "url": '/wallet',
                "icon": 'dripicons-wallet'
            }
        ]
    },
    "database": {
        "icon": """
        <svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve" sodipodi:docname="blabla.svg" inkscape:version="1.0.1 (0767f8302a, 2020-10-17)"><metadata id="metadata61"><rdf:RDF><cc:Work rdf:about=""><dc:format>image/svg+xml</dc:format><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /></cc:Work></rdf:RDF></metadata><defs id="defs59" /><sodipodi:namedview pagecolor="#ffffff" bordercolor="#666666" borderopacity="1" objecttolerance="10" gridtolerance="10" guidetolerance="10" inkscape:pageopacity="0" inkscape:pageshadow="2" inkscape:window-width="1920" inkscape:window-height="1009" id="namedview57" showgrid="false" inkscape:zoom="1.3417969" inkscape:cx="254.23646" inkscape:cy="264.35264" inkscape:window-x="0" inkscape:window-y="34" inkscape:window-maximized="1" inkscape:current-layer="Capa_1" /> <g id="g26" /> <g id="g28" /> <g id="g30" /> <g id="g32" /> <g id="g34" /> <g id="g36" /> <g id="g38" /> <g id="g40" /> <g id="g42" /> <g id="g44" /> <g id="g46" /> <g id="g48" /> <g id="g50" /> <g id="g52" /> <g id="g54" /> <path style="fill:#ffffff;stroke:none;stroke-width:1;fill-opacity:1" d="M 224.42569,169.25215 C 178.7794,165.99773 139.02198,156.57564 108.53632,141.78761 94.620715,135.03741 85.382524,128.78649 77.186799,120.57532 66.516368,109.88478 62.765227,100.46614 65.218554,90.52457 72.095533,62.657131 121.81652,37.089715 189.39804,26.669272 c 35.83245,-5.525033 79.23545,-6.367457 116.262,-2.256571 71.99963,7.993784 129.18912,33.642077 140.16265,62.860015 1.21443,3.233536 1.51211,5.449212 1.31741,9.805882 -0.37533,8.398882 -4.00683,15.315822 -12.46579,23.743702 -25.73317,25.63862 -81.21881,43.76621 -148.39127,48.4806 -12.4756,0.87558 -49.28836,0.84538 -61.85735,-0.0507 z" id="path886" /><path style="fill:#ffffff;stroke:none;stroke-width:1;fill-opacity:1" d="M 222.93515,275.8534 C 149.67692,270.10866 89.228676,247.6497 70.157472,219.09035 c -5.828965,-8.72894 -5.964676,-9.79506 -5.964676,-46.85717 v -32.71354 l 6.521106,5.13954 c 66.093998,52.09125 226.635338,63.74052 327.732168,23.78103 15.56323,-6.15151 35.23944,-17.04399 43.59825,-24.13538 5.87859,-4.98724 5.29925,-8.50164 5.05877,30.68716 l -0.21452,34.95599 -1.97488,3.89751 c -9.20012,18.15669 -33.31552,34.05425 -69.62609,45.89947 -22.31743,7.28039 -45.05896,11.87535 -74.84444,15.12241 -12.73884,1.38873 -64.04876,2.04147 -77.50801,0.98603 z" id="path888" /><path style="fill:#ffffff;stroke:none;stroke-width:1;fill-opacity:1" d="m 237.09527,383.17454 c -59.03736,-2.27005 -113.58326,-16.37681 -146.07278,-37.77759 -3.484134,-2.29499 -9.554486,-7.38323 -13.489671,-11.3072 -5.741308,-5.72494 -7.729066,-8.30443 -10.061136,-13.0562 l -2.906252,-5.9217 -0.221024,-34.52181 -0.221024,-34.5218 5.839174,4.71422 c 29.505601,23.82119 81.462993,40.6695 142.911463,46.34215 6.96827,0.64328 21.7246,1.3756 32.79185,1.62737 63.52745,1.44523 123.3436,-9.17881 166.19505,-29.51815 11.19035,-5.31148 18.84075,-9.91061 28.13391,-16.91305 l 7.26638,-5.47525 v 33.55238 c 0,30.94755 -0.10895,33.86236 -1.40341,37.54532 -8.09514,23.03213 -48.99337,45.7711 -102.56166,57.02316 -22.23249,4.66995 -43.51916,7.14392 -70.90511,8.24069 -10.18996,0.40809 -19.03026,0.69345 -19.6451,0.63413 -0.61485,-0.0593 -7.65765,-0.35933 -15.65066,-0.66667 z" id="path890" /><path style="fill:#ffffff;stroke:none;stroke-width:1;fill-opacity:1" d="M 232.62365,489.76907 C 150.42744,485.35862 82.519201,459.51482 66.995723,426.73615 l -2.430292,-5.1317 -0.221238,-34.55025 -0.221237,-34.55026 4.320218,3.72547 c 20.991574,18.10176 61.276926,34.30873 104.931576,42.21445 28.57077,5.17407 47.95694,6.75771 82.72489,6.75771 29.80439,0 39.94647,-0.60116 63.47055,-3.76213 52.61349,-7.06975 98.59778,-23.80768 124.12555,-45.18074 l 3.6083,-3.02104 -0.20773,34.96888 -0.20774,34.96888 -2.59973,5.17667 c -3.38034,6.73102 -14.30098,17.86227 -23.11206,23.5578 -30.361,19.62551 -73.52581,32.13434 -126.69577,36.71545 -16.75856,1.44392 -46.13878,1.98715 -61.85736,1.14373 z" id="path892" /></svg>
        """,
        "indexes": [
            {
                "name": 'Permissions',
                "url": '/permissions',
                "icon": 'dripicons-lock'
            },
            {
                "name": 'Countries',
                "url": '/countries',
                "icon": 'dripicons-flag'
            },
            {
                "name": 'Cities',
                "url": '/cities',
                "icon": 'dripicons-map'
            },
            {
                "name": 'Users',
                "url": '/users',
                "icon": 'dripicons-user'
            },
            {
                "name": 'PasswordRecover',
                "url": '/passwordrecover',
                "icon": 'dripicons-ticket'
            },
            {
                "name": 'AuthTokens',
                "url": '/authtokens',
                "icon": 'dripicons-ticket'
            },
            {
                "name": 'Payments',
                "url": '/payments',
                "icon": 'far fa-money-bill-alt'
            },
            {
                "name": 'Reports',
                "url": '/reports',
                "icon": 'dripicons-article'
            },
            {
                "name": 'Messages',
                "url": '/messages',
                "icon": 'dripicons-message'
            },
            {
                "name": 'Wallets',
                "url": '/wallets',
                "icon": 'dripicons-wallet'
            },
            {
                "name": 'Orders',
                "url": '/orders',
                "icon": 'dripicons-cart'
            },
            {
                "name": 'CouponCodes',
                "url": '/couponcodes',
                "icon": 'dripicons-ticket'
            }
        ]
    },
    # "account": {
    #     "icon": """
    #     <svg style="fill:white;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M337.454 232c33.599 0 61.092-27.002 61.092-60 0-32.997-27.493-60-61.092-60s-61.09 27.003-61.09 60c0 32.998 27.491 60 61.09 60zm-162.908 0c33.599 0 61.09-27.002 61.09-60 0-32.997-27.491-60-61.09-60s-61.092 27.003-61.092 60c0 32.998 27.493 60 61.092 60zm0 44C126.688 276 32 298.998 32 346v54h288v-54c0-47.002-97.599-70-145.454-70zm162.908 11.003c-6.105 0-10.325 0-17.454.997 23.426 17.002 32 28 32 58v54h128v-54c0-47.002-94.688-58.997-142.546-58.997z"></path></svg>
    #     """,
    #     "indexes": [

    #     ]
    # },
    "settings": {
        "icon": """
        <svg style="fill:white;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M413.967 276.8c1.06-6.235 1.06-13.518 1.06-20.8s-1.06-13.518-1.06-20.8l44.667-34.318c4.26-3.118 5.319-8.317 2.13-13.518L418.215 115.6c-2.129-4.164-8.507-6.235-12.767-4.164l-53.186 20.801c-10.638-8.318-23.394-15.601-36.16-20.801l-7.448-55.117c-1.06-4.154-5.319-8.318-10.638-8.318h-85.098c-5.318 0-9.577 4.164-10.637 8.318l-8.508 55.117c-12.767 5.2-24.464 12.482-36.171 20.801l-53.186-20.801c-5.319-2.071-10.638 0-12.767 4.164L49.1 187.365c-2.119 4.153-1.061 10.399 2.129 13.518L96.97 235.2c0 7.282-1.06 13.518-1.06 20.8s1.06 13.518 1.06 20.8l-44.668 34.318c-4.26 3.118-5.318 8.317-2.13 13.518L92.721 396.4c2.13 4.164 8.508 6.235 12.767 4.164l53.187-20.801c10.637 8.318 23.394 15.601 36.16 20.801l8.508 55.117c1.069 5.2 5.318 8.318 10.637 8.318h85.098c5.319 0 9.578-4.164 10.638-8.318l8.518-55.117c12.757-5.2 24.464-12.482 36.16-20.801l53.187 20.801c5.318 2.071 10.637 0 12.767-4.164l42.549-71.765c2.129-4.153 1.06-10.399-2.13-13.518l-46.8-34.317zm-158.499 52c-41.489 0-74.46-32.235-74.46-72.8s32.971-72.8 74.46-72.8 74.461 32.235 74.461 72.8-32.972 72.8-74.461 72.8z"></path></svg>
        """,
        "indexes": [
            {
                "name": 'Account Settings',
                "url": '/account-settings',
                "icon": 'dripicons-gear',
            },
            {
                "name": 'Password Recover',
                "url": '/password-recover',
                "icon": 'dripicons-lock',
            }
        ]
    },
}
