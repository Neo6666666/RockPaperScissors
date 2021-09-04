module.exports = wallaby => {
  process.env.VUE_CLI_BABEL_TRANSPILE_MODULES = true;

  return {
    files: ['src/**/*', 'jest.config.js', 'package.json', 'tsconfig.json'],

    tests: ['tests/**/*.spec.ts'],

    env: {
      type: 'node'
    },

    preprocessors: {
      '**/*.js?(x)': file => require('@babel/core').transform(
        file.content,
        {sourceMap: true, compact: false, filename: file.path, presets: [require('babel-preset-jest'), require("@babel/preset-env")]})
    },

    setup(wallaby) {
      const jestConfig = require('./package').jest || require('./jest.config');
      jestConfig.transform && delete jestConfig.transform['^.+\\.tsx?$'];
      wallaby.testFramework.configure(jestConfig);
    },

    testFramework: 'jest'
  }
}
