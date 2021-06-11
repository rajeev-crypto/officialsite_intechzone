module.exports  = function(grunt){

	grunt.initConfig({
		pkg : grunt.file.readJSON("package.json"),

		"string-replace": {
		  	inline: {
			    files: [{
			      expand: true,
			      cwd: '',
			      src: '**/*.htm',
			      dest: 'dest/'
			    }],
			    options: {
			      replacements: [
			        {
			          pattern: '<title>BOLO</title>',
			          replacement: '<title>Bolo.Cases - Твой чехол на каждый день</title>'
			        }
			      ]
			    }
			  }
		},

        uglify: {
            my_target: {
               files: {
                'js/min/file.js': ['js/file.js']
              }
            }
        },

        cssmin: {
          options: {
            shorthandCompacting: false,
            roundingPrecision: -1
          },
          target: {
            files: {
              'css/min/file.min.css': ['css/file.css']
            }
          }
        },
		
		jshint: {
			options: {
				"curly": true,
				"eqnull": true,
				"eqeqeq": true,
				"undef": true,
				"globals": {
					"jQuery": true,
					console : true
				}
			},
			"<%= pkg.name %>" : {
				src: [ "js/scripts.js" ]
			}
		},

		sass: {
		    dist: {
			  options: {
			  	style: 'expanded'
			  },
		      files: {
                'css/main.css': 'sass/main.scss',
                'css/stars.css': 'sass/stars.sass'
              }
		    }
		},

		watch: {
			src: {
				options: { livereload: true },
                files: ['*.htm']               
            },
			
			css: {
				options: { livereload: true },
				files: ["sass/*.scss"],
				tasks: ["sass"]
			}		
		},

		removelogging: { 
			dist: {
				src: "js/scripts.js",
				dest: "js/scripts.js"
			}
		},

        autoprefixer: {
            options: {
                browsers: ['last 2 versions', 'ie 9']
            },
            multiple_files: {
                src: 'css/*.css'
            }
        }

	});
	
	grunt.loadNpmTasks("grunt-string-replace");
	grunt.loadNpmTasks("grunt-contrib-jshint");
	grunt.loadNpmTasks("grunt-contrib-watch");
	grunt.loadNpmTasks("grunt-contrib-sass");
	grunt.loadNpmTasks("grunt-remove-logging");
    grunt.loadNpmTasks("grunt-contrib-uglify");
    grunt.loadNpmTasks("grunt-contrib-cssmin");
    grunt.loadNpmTasks("grunt-autoprefixer");

	grunt.registerTask("default", ["sass", "watch"]);
	grunt.registerTask("removeLog", ["removelogging"]); 
	grunt.registerTask("jshint", ["jshint"]);
    grunt.registerTask("min", ["uglify", "cssmin"]);
    grunt.registerTask("pre", ["autoprefixer"]);
    grunt.registerTask("replace", "string-replace");
};