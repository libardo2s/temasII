app.controller('ColegioController', function ($scope, ColegioService) {
    //VistaModelo
    $scope.Colegio = {}; //Objeto Actual
    $scope.Colegios = []; //Listado de Objetos
    $scope.editMode = false; // Modo de Edición
    //Cargar los datos
    loadRecords();
    //Function to Reset Scope variables
    function initialize() {
        $scope.Colegio = {};
        $scope.Colegio.nombre = "";
        $scope.Colegio.direccion = "";
        $scope.Colegio.codigo = "";
    }
    //Function to load all Employee records
    function loadRecords() {
        var promiseGet = ColegioService.getall(); //The Method Call from service
        promiseGet.then(function (pl) {$scope.Colegios = pl.data;},
              function (errorPl) {
                  $log.error('failure loading Contactos', errorPl);
              });
    }


    $scope.get = function () {
         $scope.Colegio = this.Colegio;
         $('#simpleModal').modal('show');
    }
    //Function to Cancel Form
    

});

