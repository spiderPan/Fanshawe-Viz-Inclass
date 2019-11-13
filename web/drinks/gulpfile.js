const gulp = require("gulp");
const browserSync = require("browser-sync").create();

//Browser Reload Function
gulp.task("reload", function(done) {
  browserSync.reload();
  done();
});

gulp.task("default", function() {
  browserSync.init({
    server: "./",
    port: 4000
  });

  gulp.watch("js/*.js", gulp.series(["reload"]));
  gulp.watch("css/*.css", gulp.series(["reload"]));
});
