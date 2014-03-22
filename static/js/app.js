var xlplotApp = angular.module('xlplotApp', []);

xlplotApp.controller('UploadFormController', 
  function($scope, $fileUpload, $mapService) {

    $scope.onSubmit = function() {
      var file = $scope.excelFileInput;
      var uploadUrl = '/api/upload';
      $fileUpload.uploadFileToUrl(file, uploadUrl)
        .success(function(data, status, headers, config) {
          $mapService.addMarkers(data.locations);
        })
        .error(function(data, status, headers, config) {
          alert(data);
        });
    };
  })

/*
 * fileModel and $fileUpload were found online,
 * will update with source when I can
 */
.directive('fileModel', ['$parse', function ($parse) {
  return {
    restrict: 'A',
    link: function(scope, element, attrs) {
      var model = $parse(attrs.fileModel);
      var modelSetter = model.assign;
      
      element.bind('change', function(){
        scope.$apply(function(){
          modelSetter(scope, element[0].files[0]);
        });
      });
    }
  };
}])

.service('$fileUpload', ['$http', function ($http) {
  var that = this;

  that.uploadFileToUrl = function(file, uploadUrl){
    var fd = new FormData();
    fd.append('file', file);
    return($http.post(uploadUrl, fd, {
      transformRequest: angular.identity,
      headers: {'Content-Type': undefined}
    }));
  };
}])

.service('$mapService', function($rootScope) {
  var that = this;

  that.addMarkers = function(locs) {
    locs.forEach(function(item) {
      console.log(item);
      var marker = new google.maps.Marker({    
        position: new google.maps.LatLng(item.lat, item.lng),
        map: $rootScope.map
      });
    });
  };
})

/*
 * Run the app!
 */
.run(function($rootScope) {
  var mapOptions = {
    zoom: 3, 
    center: new google.maps.LatLng(37.774546, -122.433523),
  };

  var mapCanvas = document.getElementById('map-canvas');
  $rootScope.map = new google.maps.Map(mapCanvas, mapOptions);
});
