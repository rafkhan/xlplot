var xlplotApp = angular.module('xlplotApp', []);

xlplotApp.controller("MapListCtrl", function MapListCtrl($scope, $http) {
	$http.get("/map").success(function(data) {
		$scope.maplist = data;
	});
});
