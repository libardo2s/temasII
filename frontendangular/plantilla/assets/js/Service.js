app.service("ColegioService", function ($http) {
    var url="https://reinarbackend.herokuapp.com";
    
    this.getitem = function (item) {
        var req = $http.get(url+"/api/colegio/"+ item);
        return req;
    };
    
    this.getall = function () {
        var req = $http.get(url+"/api/colegio/");
        return req;
    };
    
    this.post = function (colegio) {
        var req = $http.post(url+'/api/colegio/', colegio);
        return req;
    };
    
    this.put = function (cod,colegio) {
        var request = $http({
            method: "put",
            url: url+'/api/colegio/'+ cod,
            data: colegio
        });
        return request;
    };
    
});