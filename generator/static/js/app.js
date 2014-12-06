(function(){
    var app = angular.module('ipsum', []);

    var API_URL = "http://en.wikiquote.org/w/api.php?callback=JSON_CALLBACK";

    app.controller('GeneratorController', function($scope, $http){
        var generator = this;

        // attributes //

        this.query = ""; // user-input query
        this.words = 500; // default number of words
        this.results = []; // search results from wiki api


        // methods //

        this.generateIpsum = function(page, words) {
            $http.get('/api/generate-ipsum/', {params: {page: page.pageid, words: generator.words}}).success(function(data){
                console.log(data);
            });
        }

        $scope.$watch(
            function(){ return generator.query },
            function(){
                $http.jsonp(API_URL, {params: {format: 'json', action: 'query', redirects: '1', titles: generator.query}}).success(function(data){
                    generator.results = data.query.pages;
                    console.log(generator.results);
                });
            }
        );
    });
})();
