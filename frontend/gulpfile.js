const { src, dest, series, watch } = require('gulp'),
  concat = require('gulp-concat'),
  htmlMin = require('gulp-htmlmin'),
  autoPrefixer = require('gulp-autoprefixer'),
  cleanCSS = require('gulp-clean-css'),
  svgSprite = require('gulp-svg-sprite'),
  sourceMaps = require('gulp-sourcemaps'),
  del = require('del'),
  sass = require('gulp-sass')(require('sass')),
  strip = require('gulp-strip-comments'),
  webpack = require('webpack-stream'),
  browserSync = require('browser-sync').create();

const clean = () => {
  return del(['dist',
    'prod',
  ])
}

const resources = () => {
  return src('src/resources/**')
    .pipe(dest('prod/resources'))
    .pipe(dest('dist/resources'))
}

const htmlMinify = () => {
  return src('src/**/*.html')
    .pipe(htmlMin({
      collapseWhitespace: true,
    }))
    .pipe(strip())
    .pipe(dest('prod'))
    .pipe(dest('dist'))
    .pipe(browserSync.stream())
}

const scssStyles = () => {
  return src('src/styles/main.scss')
    .pipe(sourceMaps.init())
    .pipe(sass({
    }).on('error', sass.logError))
    .pipe(autoPrefixer({
      cascade: false,
    }))
    .pipe(cleanCSS({
      level: {
        1: {
          specialComments: 0
        }
      }
    }))
    .pipe(dest('prod'))
    .pipe(sourceMaps.write())
    .pipe(dest('dist'))
    .pipe(browserSync.stream())
}

const scriptsProd = () => {
  return src('src/scripts/main.js')
    .pipe(webpack({
      mode: 'production',
    }))
    .pipe(dest('prod'))
    .pipe(browserSync.stream())
}

const scriptsDist = () => {
  return src('src/scripts/main.js')
    .pipe(webpack({
      mode: 'development',
      devtool: 'source-map'
    }))
    .pipe(dest('dist'))
    .pipe(browserSync.stream())
}

const scriptsLib = () => {
  return src('src/scripts/libs/*.js')
    .pipe(sourceMaps.init())
    .pipe(concat('lib.js'))
    .pipe(strip())
    .pipe(dest('prod'))
    .pipe(sourceMaps.write())
    .pipe(dest('dist'))
    .pipe(browserSync.stream())
}

const svgSprites = () => {
  return src('src/img/svg/*.svg')
    .pipe(svgSprite({
      mode: {
        stack: {
          sprite: '../sprite.svg'
        }
      }
    }))
    .pipe(dest('prod/img'))
    .pipe(dest('dist/img'))
}

const image = () => {
  return src(['src/img/*.jpg',
  'src/img/*.webp',
  'src/img/*.png',
  'src/img/*.svg',
  ])
  .pipe(dest('prod/img'))
  .pipe(dest('dist/img'))
  .pipe(browserSync.stream())
}

const fonts = () => {
  return src([
    'src/fonts/**/*.woff',
    'src/fonts/**/*.woff2'
  ])
    .pipe(dest('prod/fonts'))
    .pipe(dest('dist/fonts'))
}

const watchFiles = () => {
  browserSync.init({
    server: {
      baseDir: 'dist'
    }
  })
}

watch('src/**/*.html', htmlMinify)
watch('src/img/svg/**/*.svg', svgSprites)
watch(['src/scripts/components/*.js',
  'src/scripts/main.js'], scriptsProd)
watch(['src/scripts/components/*.js',
  'src/scripts/main.js'], scriptsDist)
watch('src/scripts/libs/*.js', scriptsLib)
watch('src/resources/**', resources)
watch('src/styles/**/*.scss', scssStyles)

exports.clean = clean
exports.scripts = scriptsDist
exports.scssStyles = scssStyles
exports.htmlMinify = htmlMinify
exports.default = series(clean, resources, htmlMinify, scssStyles, scriptsProd, scriptsDist, scriptsLib, svgSprites, image, fonts, watchFiles)