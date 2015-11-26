miapp=angular.module('MyApp.controllers', []);

miapp.controller('controlador', function ($scope) {
         $scope.mensaje="deiner";
  });

miapp.controller('json', function($scope, $http) {
    $http.get("http://www.w3schools.com/angular/customers.php")
    .success(function(response) {
            $scope.names = response.records;
        });
});

miapp.controller('json1', function($scope, $http) {
    $http.get("https://restcountries.eu/rest/v1/all")
    .success(function(response) {
            $scope.name = response;
        });
});

miapp.controller('DRF', function($scope, $http) {
    $scope.Colegio = {}; //Objeto Actual
    var url="https://reinarbackend.herokuapp.com/api/colegio/";

    $http.get(url)
    .success(function(response) {
            $scope.name = response;
        });
   
   $scope.getitem=function(item){
       $http.get(url+item)
           
           .success(function(response){
              
               $scope.Colegio.codigo =response.codigo;
               $scope.Colegio.nombre =response.nombre;
               $scope.Colegio.telefono =response.telefono;
               $scope.Colegio.direccion=response.direccion;
               $scope.Colegio.estado=response.estado;
               $('#detalleModal').modal('show');
           
           });

   };
    
    $scope.showmodal=function(){ 
    $('#formModal').modal('show');
        
    };

   $scope.showdelete=function(item){ 
    $('#simpleModal').modal('show');  
        $http.get(url+item)
           
           .success(function(response){
              
               $scope.Colegio.codigo =response.codigo;
               
      });
    };
    
    $scope.delete=function(){ 
        var cod=$scope.Colegio.codigo;
     
     $http.delete(url+cod+"/")
     
     .success(function(){
     $('#simpleModal').modal('hide');  
     });
    };
    
    
    $scope.add=function(){ 
        var colegio = {};
          colegio.codigo=$scope.Colegio.codigo;
          colegio.nombre=$scope.Colegio.nombre;
          colegio.telefono=$scope.Colegio.telefono;
          colegio.direccion=$scope.Colegio.direccion;
          colegio.estado="Moroso";
        $http.post(url,colegio);
    $('#formModal').modal('hide');  
   };

 
});

miapp.controller('alerta', function($scope) {
    $scope.mensaje="hola deiner"
        $scope.Show=function(){
            alert($scope.mensaje);
        };

});
