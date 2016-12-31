var artistControllers = angular.module('artistControllers', []);

artistControllers.controller('ListController', ['$scope', '$http', function($scope, $http) {
  $http.get('js/data.json').success(function(data) {
    $scope.artists = data;
    $scope.artistOrder = 'name';
  });
}]);

artistControllers.controller('DetailsController', ['$scope', '$http','$routeParams', function($scope, $http, $routeParams) {
  $http.get('js/data.json').success(function(data) {
    $scope.artists = data;
    $scope.whichItem = $routeParams.itemId;

    $scope.nextArtist = ($routeParams.itemId+1) % data.length;
    if($routeParams.itemId == 0){
       $scope.prevArtist =data.length-1;
    }else{
       $scope.prevArtist = ($routeParams.itemId-1) % data.length;
    }
   
    
  });
}]);

