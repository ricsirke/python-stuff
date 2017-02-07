var x = d3.scaleLinear()
                .domain([0, this.n - 1])
                .range([0, this.width]);
                
var y = d3.scaleLinear()
        .domain([-260, 260])
        .range([this.height, 0]);



var Graph = {
    

    initVars: function(){
        this.n = 1000;
        this.data = [];
        
        for (var i=0; i<this.n; i++){
            this.data.push(0);
        }
        
        this.svg =        d3.select("svg");
        this.margin =     {top: 20, right: 20, bottom: 20, left: 40};
        this.width =      this.svg.attr("width") - this.margin.left - this.margin.right;
        this.height =     this.svg.attr("height") - this.margin.top - this.margin.bottom;
        this.g =          this.svg.append("g").attr("transform", "translate(" + this.margin.left + "," + this.margin.top + ")");
              
        
                
        this.line = d3.line()
                .x(function(d, i) { return x(i); })
                .y(function(d, i) { return y(d); });
    },
    
    onNewData: function(inData){
        var newData = JSON.parse(inData).data;        
        newData = newData.map( function(a) {return parseInt(a, 10);} );
        
        for (var i=0; i<10; i++){
            this.data.push(newData.pop());
            this.tick();
        }
        
        // this.data = this.data.concat(newData);
        // this.data = this.data.slice(newData.length, this.data.length);
        // this.tick();

        
    },
    
    connect: function() {
        var webaddr = "http://localhost:5000/";
        var sock = io(webaddr);

        var that = this;
        sock.on("newdata", jQuery.proxy(this.onNewData, this));
    },
    
    
    initGraph: function(){
            
        this.g.append("defs").append("clipPath")
            .attr("id", "clip")
          .append("rect")
            .attr("width", this.width)
            .attr("height", this.height);
        this.g.append("g")
            .attr("class", "axis axis--x")
            .attr("transform", "translate(0," + y(0) + ")")
            .call(d3.axisBottom(x));
            
        this.g.append("g")
            .attr("class", "axis axis--y")
            .call(d3.axisLeft(y));
            
        this.g.append("g")
            .attr("clip-path", "url(#clip)")
          .append("path")
            .datum(this.data)
            .attr("class", "line")
          .transition()
            .duration(500)
            .ease(d3.easeLinear);
    },
    
    
    tick: function() {
          // Push a new data point onto the back.
          //data.push(255*random());
          // Redraw the line.
          // d3.select($(".line")[0])
              // .attr("d", this.line)
              // .attr("transform", null);
              
          // Slide it to the left.
          var trans = d3.active($(".line")[0]);
          
          // if (trans){
              // trans
                // .attr("transform", "translate(" + x(-1) + ",0)")
                // .transition();
          // }
          // else {
              d3.select($(".line")[0])
                .attr("transform", "translate(" + x(-1) + ",0)");
          // }
          
              
          // Pop the old data point off the front.
          //data.shift();
        }
    
    
}

Graph.initVars();
Graph.initGraph();
Graph.connect();


















function connect(){
    var webaddr = "http://localhost:5000/";
    var sock = io(webaddr);
    function onNewData(data){
        newData = JSON.parse(data).data;        
        newData = newData.map( function(x) {return parseInt(x, 10);} );
        
        console.log(newData);
        
    }
    sock.on("newdata", onNewData);
}



function initGraph(){
   
    var n = 40,
        random = d3.randomNormal(0, .2),
        data = d3.range(n).map(function(x){return 0;});
        
    var svg = d3.select("svg"),
        margin = {top: 20, right: 20, bottom: 20, left: 40},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        
    var x = d3.scaleLinear()
        .domain([0, n - 1])
        .range([0, width]);
        
    var y = d3.scaleLinear()
        .domain([-260, 260])
        .range([height, 0]);
        
    var line = d3.line()
        .x(function(d, i) { return x(i); })
        .y(function(d, i) { return y(d); });
        
    g.append("defs").append("clipPath")
        .attr("id", "clip")
      .append("rect")
        .attr("width", width)
        .attr("height", height);
    g.append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + y(0) + ")")
        .call(d3.axisBottom(x));
        
    g.append("g")
        .attr("class", "axis axis--y")
        .call(d3.axisLeft(y));
        
    g.append("g")
        .attr("clip-path", "url(#clip)")
      .append("path")
        .datum(this.data)
        .attr("class", "line")
      .transition()
        .duration(500)
        .ease(d3.easeLinear)
        .on("start", tick);
        
    function tick() {
      // Push a new data point onto the back.
      data.push(255*random());
      // Redraw the line.
      d3.select(this)
          .attr("d", line)
          .attr("transform", null);
          
      // Slide it to the left.
      d3.active(this)
          .attr("transform", "translate(" + x(-1) + ",0)")
        .transition()
          .on("start", tick);
          
      // Pop the old data point off the front.
      data.shift();
    }
}

//connect();
//initGraph();

