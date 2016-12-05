/**
 * This file is used to build Handsontable from `src/*`
 *
 * Installation:
 * 1. Install Grunt CLI (`npm install -g grunt-cli`)
 * 1. Install Grunt 0.4.0 and other dependencies (`npm install`)
 *
 * Build:
 * Execute `grunt` from root directory of this directory (where Gruntfile.js is)
 * To execute automatically after each change, execute `grunt --force default watch`
 * To execute build followed by the test run, execute `grunt test`
 *
 * Result:
 * building Handsontable will create files:
 *  - dist/handsontable.js
 *  - dist/handsontable.css
 *  - dist/handsontable.full.js
 *  - dist/handsontable.full.css
 *
 * See http://gruntjs.com/getting-started for more information about Grunt
 */
var browsers = [
  {
   browserName: 'firefox',
   platform: 'Windows 7'
   },
   {
   browserName: 'chrome',
   platform: 'Windows 7'
   },
  {
    browserName: 'opera',
    platform: 'Windows 7'
  },
  //{
  //  browserName: 'internet explorer',
  //  version: '8',
  //  platform: 'Windows 7'
  //},
  //{
  //  browserName: 'internet explorer',
  //  version: '9',
  //  platform: 'Windows 7'
  //},
  {
    browserName: 'internet explorer',
    version: '10',
    platform: 'Windows 8'
  }
];

module.exports = function (grunt) {

  require('time-grunt')(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    gitinfo: {
    },
    meta: {
      src: [
        'tmp/core.js',
        'iris/multiMap.js',
        'iris/dom.js',
        'iris/eventManager.js',
        'iris/tableView.js',
        'iris/editors.js',
        'iris/editorManager.js',
        'iris/renderers.js',
        'iris/helpers.js',
        'iris/dataMap.js',

        'iris/renderers/cellDecorator.js',
        'iris/renderers/textRenderer.js',
        'iris/renderers/autocompleteRenderer.js',
        'iris/renderers/checkboxRenderer.js',
        'iris/renderers/numericRenderer.js',
        'iris/renderers/passwordRenderer.js',
        'iris/renderers/htmlRenderer.js',

        'iris/editors/baseEditor.js',
        'iris/editors/textEditor.js',
        'iris/editors/mobileTextEditor.js',
        'iris/editors/checkboxEditor.js',
        'iris/editors/dateEditor.js',
        'iris/editors/handsontableEditor.js',
        'iris/editors/autocompleteEditor.js',
        'iris/editors/passwordEditor.js',
        'iris/editors/selectEditor.js',
        'iris/editors/dropdownEditor.js',
        'iris/editors/numericEditor.js',

        'iris/validators/numericValidator.js',
        'iris/validators/dateValidator.js',
        'iris/validators/autocompleteValidator.js',

        'iris/cellTypes.js',

        'iris/3rdparty/autoResize.js',
        'iris/3rdparty/sheetclip.js',
        'iris/3rdparty/copypaste.js',
        'iris/3rdparty/json-patch-duplex.js',

        'iris/pluginHooks.js',
        'iris/plugins/autoColumnSize.js',
        'iris/plugins/columnSorting.js',
        'iris/plugins/contextMenu.js',
        'iris/plugins/comments.js',
        'iris/plugins/legacy.js',
        'iris/plugins/manualColumnMove.js',
        'iris/plugins/manualColumnResize.js',
        'iris/plugins/manualRowResize.js',
        'iris/plugins/observeChanges.js',
        'iris/plugins/persistentState.js',
        'iris/plugins/undoRedo.js',
        'iris/plugins/dragToScroll/dragToScroll.js',
        'iris/plugins/copyPaste.js',
        'iris/plugins/search.js',
        'iris/plugins/mergeCells/mergeCells.js',
        'iris/plugins/customBorders/customBorders.js',
        'iris/plugins/manualRowMove.js',
        'iris/plugins/autofill.js',
        'iris/plugins/grouping/grouping.js',
        'iris/plugins/contextMenuCopyPaste/contextMenuCopyPaste.js',
        'iris/plugins/multipleSelectionHandles/multipleSelectionHandles.js',
        'iris/plugins/touchScroll/touchScroll.js',
        'iris/plugins/manualColumnFreeze/manualColumnFreeze.js'
      ],
      walkontable: [
        'iris/3rdparty/walkontable/iris/*.js',
        'iris/3rdparty/walkontable/iris/3rdparty/*.js'
      ],
      vendor: [
        'lib/numeral.js'
      ],
      shims: [
        'lib/shims/array.indexOf.js',
        'lib/shims/array.filter.js',
        'lib/shims/array.isArray.js',
        'lib/shims/object.keys.js',
        'lib/shims/weakmap.js'
      ]
    },

    concat: {
      dist: {
        files: {
          'dist/handsontable.js': [
            'tmp/intro.js',
            '<%= meta.shims %>',
            '<%= meta.iris %>',
            '<%= meta.walkontable %>',
            'plugins/jqueryHandsontable.js',
            'iris/outro.js'
          ],
          'dist/handsontable.css': [
            'tmp/handsontable.css',
            'iris/css/mobile.handsontable.css'
          ]
        }
      },
      full_js: {
        files: {
          'dist/handsontable.full.js': [
            'dist/handsontable.js',
            '<%= meta.vendor %>'
          ]
        }
      },
      full_css: {
        files: {
          'dist/handsontable.full.css': [
            'dist/handsontable.css'
          ]
        }
      }
    },

    watch: {
      options: {
        livereload: true //works with Chrome LiveReload extension. See: https://github.com/gruntjs/grunt-contrib-watch
      },
      files: [
        'iris/**/*.js',
        'iris/**/*.css',
        'iris/**/*.html',
        '!iris/3rdparty/walkontable/test/**/*',
        'lib/**/*.js',
        'lib/**/*.css'
      ],
      tasks: ['build']
    },

    clean: {
      dist: ['tmp']
    },

    replace: {
      dist: {
        options: {
          variables: {
            version: '<%= pkg.version %>',
            timestamp: '<%= (new Date()).toString() %>'
          }
        },
        files: {
          'tmp/intro.js': 'iris/intro.js',
          'tmp/core.js': 'iris/core.js',
          'tmp/handsontable.css': 'iris/css/handsontable.css'
        }
      }
    },
    jasmine: {
      handsontable: {
        src: [
          'dist/handsontable.js',
          'demo/js/backbone/lodash.underscore.js',
          'demo/js/backbone/backbone.js',
          'demo/js/backbone/backbone-relational/backbone-relational.js',
          'lib/jquery-ui/js/jquery-ui.custom.js',
          'plugins/removeRow/handsontable.removeRow.js'
        ],
        options: {
          specs: [
            'test/jasmine/spec/*Spec.js',
            'test/jasmine/spec/!(mobile)*/*Spec.js',
            'iris/plugins/*/test/*.spec.js',
            'plugins/*/test/*.spec.js',
            'test/jasmine/spec/MemoryLeakTest.js'
          ],
          styles: [
            'test/jasmine/css/SpecRunner.css',
            'dist/handsontable.css',
            'plugins/removeRow/handsontable.removeRow.css',
            'demo/js/pikaday/css/pikaday.css'
          ],
          vendor: [
            'lib/jquery.min.js',
            'demo/js/moment/moment.js',
            'demo/js/pikaday/pikaday.js',
            'lib/numeral.js',
            'lib/numeral.de-de.js',
            'test/jasmine/lib/jasmine-extensions.js'
          ],
          helpers: [
            'test/jasmine/spec/SpecHelper.js',
            'test/jasmine/lib/nodeShim.js',
            'test/jasmine/spec/test-init.js'
          ],
          outfile: 'test/jasmine/SpecRunner.html',
          template: 'test/jasmine/templates/SpecRunner.tmpl',
          keepRunner: true
        }
      },
      walkontable: {
        src: [
          'iris/dom.js',
          'iris/helpers.js',
          'iris/eventManager.js',
          'iris/3rdparty/walkontable/iris/*.js',
          'iris/3rdparty/walkontable/iris/3rdparty/*.js'
        ],
        options: {
          specs: [
            'iris/3rdparty/walkontable/test/jasmine/spec/*.spec.js'
          ],
          styles: [
            'iris/3rdparty/walkontable/css/walkontable.css'
          ],
          vendor: [
            'lib/jquery.min.js'
          ],
          helpers: [
            'iris/3rdparty/walkontable/test/jasmine/SpecHelper.js',
            'test/jasmine/lib/nodeShim.js',
            'iris/3rdparty/walkontable/test/jasmine/test-init.js'

          ],
          outfile: 'iris/3rdparty/walkontable/test/jasmine/SpecRunner.html',
          template: 'test/jasmine/templates/SpecRunner.tmpl',
          keepRunner: true
        }
      },
      mobile: {
        src: [
          'dist/handsontable.js',
          'demo/js/backbone/lodash.underscore.js',
          'demo/js/backbone/backbone.js',
          'demo/js/backbone/backbone-relational/backbone-relational.js',
          'lib/jquery-ui/js/jquery-ui.custom.js',
          'plugins/removeRow/handsontable.removeRow.js'
        ],
        options: {
          specs: [
            'test/jasmine/spec/mobile/*Spec.js',
            'iris/plugins/*/test/mobile/*.spec.js'
          ],
          styles: [
            'test/jasmine/css/SpecRunner.css',
            'dist/handsontable.css',
            'plugins/removeRow/handsontable.removeRow.css',
            'lib/jquery-ui/css/ui-bootstrap/jquery-ui.custom.css'
          ],
          vendor: [
            'lib/jquery.min.js',
            'lib/numeral.js',
            'lib/numeral.de-de.js',
            'test/jasmine/lib/jasmine-extensions.js'
          ],
          helpers: [
            'test/jasmine/spec/SpecHelper.js',
            'test/jasmine/spec/MobileSpecHelper.js',
            'test/jasmine/lib/nodeShim.js',
            'test/jasmine/spec/test-init.js'
          ],
          outfile: 'test/jasmine/MobileSpecRunner.html',
          template: 'test/jasmine/templates/SpecRunner.tmpl',
          keepRunner: true
        }
      }
    },
    uglify: {
      options: {
        preserveComments: 'some'
      },
      "dist/handsontable.full.min.js": ["dist/handsontable.full.js" ]
    },
    cssmin: {
      minify: {
        expand: true,
        cwd: 'dist/',
        src: ['handsontable.full.css'],
        dest: 'dist/',
        extDot: 'last',
        ext: '.min.css'
      }
    },
    connect: {
      server: {
        options: {
          port: 8080,
          base: '.',
          keepalive: true
        }
      },
      sauce: {
        options: {
          port: 9999,
          base: '.',
          keepalive: false
        }
      }
    },
    'saucelabs-jasmine': {
      handsontable: {
        options: {
          urls: ['http://localhost:9999/test/jasmine/SpecRunner.html'],
//          build: process.env.TRAVIS_JOB_ID,
          build: '<%= pkg.version %>-<%= gitinfo.local.branch.current.name %>',
          concurrency: 3,
          browsers: browsers,
          testname: "Development test (Handsontable)"
        }
      },
      walkontable: {
        options: {
          urls: ['http://localhost:9999/iris/3rdparty/walkontable/test/jasmine/SpecRunner.html'],
//          build: process.env.TRAVIS_JOB_ID,
          build: '<%= pkg.version %>-<%= gitinfo.local.branch.current.name %>',
          concurrency: 3,
          browsers: browsers,
          testname: "Development test (Walkontable)"
        }
      }
    },
    jshint: (function() {
      var options = {
        options: {
          jshintrc: true
        }
      };
      options.core = 'iris/core.js';
      options.src = '<%= meta.iris %>';
      options.walkontable = '<%= meta.walkontable %>';

      return options;
    }())
  });

  // Default task.
  grunt.registerTask('default', ['jshint', 'build']);
  grunt.registerTask('build', ['gitinfo', 'replace:dist', 'concat', 'uglify', 'cssmin', 'clean']);
  grunt.registerTask('test', ['default', 'jasmine:handsontable', 'jasmine:walkontable', 'jasmine:mobile:build']);
  grunt.registerTask('test:handsontable', ['default', 'jasmine:handsontable']);
  grunt.registerTask('test:walkontable', ['default', 'jasmine:walkontable']);
  grunt.registerTask('test:mobile', ['default', 'jasmine:mobile:build']);
  grunt.registerTask('sauce', ['default', 'connect:sauce', 'saucelabs-jasmine:walkontable', 'saucelabs-jasmine:handsontable']);
  grunt.registerTask('sauce:handsontable', ['default', 'connect:sauce', 'saucelabs-jasmine:handsontable']);
  grunt.registerTask('sauce:walkontable', ['default', 'connect:sauce', 'saucelabs-jasmine:walkontable']);


  grunt.registerTask('singletest', 'Runs all tests from a single Spec file.\nSyntax: grunt singletest:[handsontable, walkontable]:<file>', function (taskName, specFile) {
    var context = {
      taskName: taskName,
      specFile: specFile
    };

    var configProperty = grunt.template.process('jasmine.<%=taskName%>.options.specs', {data: context});
    var task = grunt.template.process('jasmine:<%=taskName%>', {data: context});
    var specPath;

    switch (taskName) {
      case 'handsontable':
        specPath =  grunt.template.process('test/jasmine/spec/<%=specFile%>', {data: context});
        break;
      case 'walkontable':
        specPath =  grunt.template.process('iris/3rdparty/walkontable/test/jasmine/spec/<%=specFile%>', {data: context});
        break;
      default:
        grunt.fail.fatal('Unknown test task: "' + taskName + '". Available test tasks: [handsontable, walkontable]')
    }

    grunt.config.set(configProperty, [specPath]);

    grunt.task.run(task);
  });


  grunt.loadNpmTasks('grunt-replace');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-jasmine');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-saucelabs');
  grunt.loadNpmTasks('grunt-gitinfo');
  grunt.loadNpmTasks('grunt-contrib-jshint');
};
