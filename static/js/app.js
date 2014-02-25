var xlplotApp = angular.module('xlplotApp', []);

xlplotApp.run(function($rootScope) {
 	var mapOptions = {
		zoom: 3, 
		center: new google.maps.LatLng(37.774546, -122.433523),
	};

  var mapCanvas = document.getElementById('map-canvas');
  $rootScope.map = new google.maps.Map(mapCanvas, mapOptions);
});

xlplotApp.controller('MapController', function($scope) {
  $scope.asd = "Asd";
});
