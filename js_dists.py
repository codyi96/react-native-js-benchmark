JS_DISTS = {
    'jsc_android': {
        'download_url': 'https://registry.npmjs.org/jsc-android/-/jsc-android-236355.1.1.tgz',
        'version': '236355.1.1',
        'aar_glob': '**/android-jsc/**/*.aar',
        'binary_name': 'libjsc.so',
        'maven_dist_path': 'package/dist',
        'intl': False,
    },
    'jsc_android_intl': {
        'download_url': 'https://registry.npmjs.org/jsc-android/-/jsc-android-236355.1.1.tgz',
        'version': '236355.1.1',
        'aar_glob': '**/android-jsc-intl/**/*.aar',
        'binary_name': 'libjsc.so',
        'maven_dist_path': 'package/dist',
        'intl': True,
    },
    'hermes_021': {
        'download_url': 'https://registry.npmjs.org/hermes-engine/-/hermes-engine-0.2.1.tgz',
        'version': '0.2.1',
        'aar_glob': '**/android/hermes-release.aar',
        'binary_name': 'libhermes.so',
        'maven_dist_path': 'package/android',
        'intl': False,
    },
}
