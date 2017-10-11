var labelType, useGradients, nativeTextSupport, animate;

(function() {
  var ua = navigator.userAgent,
      iStuff = ua.match(/iPhone/i) || ua.match(/iPad/i),
      typeOfCanvas = typeof HTMLCanvasElement,
      nativeCanvasSupport = (typeOfCanvas == 'object' || typeOfCanvas == 'function'),
      textSupport = nativeCanvasSupport 
        && (typeof document.createElement('canvas').getContext('2d').fillText == 'function');
  //I'm setting this based on the fact that ExCanvas provides text support for IE
  //and that as of today iPhone/iPad current text support is lame
  labelType = (!nativeCanvasSupport || (textSupport && !iStuff))? 'Native' : 'HTML';
  nativeTextSupport = labelType == 'Native';
  useGradients = nativeCanvasSupport;
  animate = !(iStuff || !nativeCanvasSupport);
})();

var Log = {
  elem: false,
  write: function(text){
    if (!this.elem) 
      this.elem = document.getElementById('log');
    this.elem.innerHTML = text;
    this.elem.style.left = (500 - this.elem.offsetWidth / 2) + 'px';
  }
};


function init(param){
  //init data
  var json1 = {
    "children": [
       {
         "children": [
           {
             "children": [], 
             "data": {
               "description": "I should be able to classify polynomials and degrees.", 
               "$angularWidth": 1000, 
               "days": 111, 
               "$color": "#B0AAF6", 
               "size": 200
             }, 
             "id": "Source/Algebra/ClassifyPoly", 
             "name": "Classify Poly"
           }, 
           {
             "children": [], 
             "data": {
               "description": "I should be able to factorize a polynomial.", 
               "$angularWidth": 1000, 
               "days": 2, 
               "$color": "#B0AAF6", 
               "size": 200
             }, 
             "id": "Source/Algebra/FactorizePoly", 
             "name": "Factorize Poly"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to solve linear equations in one variable.", 
               "$angularWidth": 1000, 
               "days": 2, 
               "$color": "#B0AAF6", 
               "size": 200
             }, 
             "id": "Source/Algebra/linearOne", 
             "name": "Linear One"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to solve linear equations in two variables.", 
               "$angularWidth": 1000, 
               "days": 2, 
               "$color": "#B0AAF6", 
               "size": 200
             }, 
             "id": "Source/Algebra/LinearTwo", 
             "name": "Linear Two"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to know the algebraic identities and use them to solve problems", 
               "$angularWidth": 1000, 
               "days": 2, 
               "$color": "#B0AAF6", 
               "size": 200
             }, 
             "id": "Source/Algebra/AlgebraicEq", 
             "name": "Alg. Equations"
           }
         ], 
         "data": {
           "description": "Algebra Chapter", 
           "$color": "#dd3333", 
           "days": 2, 
           "$angularWidth": 7000, 
           "size": 2000
         }, 
         "id": "Source/Algebra", 
         "name": "Algebra"
       }, 
       {
         "children": [
           {
             "children": [], 
             "data": {
               "description": "I should be able to find Measures of Central Tendency : Mean, Median and Mode", 
               "$angularWidth": 1500, 
               "days": 3, 
               "$color": "#B0AAF6", 
               "size": 14952
             }, 
             "id": "Source/Statistics/Measures", 
             "name": "Stat. Measures"
           }, 
           {
             "children": [], 
             "data": {
               "description": "I should be able to draw Histogram, Frequency Polygon", 
               "$angularWidth": 1500, 
               "days": 111, 
               "$color": "#B0AAF6", 
               "size": 5838
             }, 
             "id": "Source/Statistics/Graphs", 
             "name": "Stat. Graphs"
           }
         ], 
         "data": {
           "description": "Statistics Chapter", 
           "$color": "#DD3333", 
           "days": 3, 
           "$angularWidth": 4000, 
           "size": 35549
         }, 
         "id": "Source/Statistics", 
         "name": "Statistics"
       },       
       {
         "children": [
           {
             "children": [], 
             "data": {
               "description": "I should be able to construct a perpendicular bisector.", 
               "$angularWidth": 1000, 
               "days": 26, 
               "$color": "#B0AAF6", 
               "size": 8079
             }, 
             "id": "Source/PracGeo/Perpendicular", 
             "name": "Perp. Bisector"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to construct incentre.", 
               "$angularWidth": 1000, 
               "days": 26, 
               "$color": "#B0AAF6", 
               "size": 8079
             }, 
             "id": "Source/PracGeo/Incentre", 
             "name": "Incentre"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to construct a centroid.", 
               "$angularWidth": 1000, 
               "days": 26, 
               "$color": "#B0AAF6", 
               "size": 8079
             }, 
             "id": "Source/PracGeo/Centroid", 
             "name": "Centroid"
           }
         ], 
         "data": {
           "description": "Practical Geometry Chapter", 
           "$color": "#DD3333", 
           "days": 26, 
           "$angularWidth": 4000, 
           "size": 8079
         }, 
         "id": "Source/PracGeo", 
         "name": "Prac. Geometry"
       }, 
       {
         "children": [
           {
             "children": [], 
             "data": {
               "description": "I should be able to understand and use Trigonometric Ratios to solve problems.", 
               "$angularWidth": 1500, 
               "days": 112, 
               "$color": "#B0AAF6", 
               "size": 1200
             }, 
             "id": "Source/Trigonometry/TrigonometryRatios", 
             "name": "Ratios"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to understand Trigonometric Ratios of Complementary Angles and solve them.", 
               "$angularWidth": 1500, 
               "days": 112, 
               "$color": "#B0AAF6", 
               "size": 1200
             }, 
             "id": "Source/Trigonometry/TrigonometryComplementary", 
             "name": "Compl. Angles"
           },
           {
             "children": [], 
             "data": {
               "description": "I should be able to know Trigonometric Table.", 
               "$angularWidth": 1500, 
               "days": 112, 
               "$color": "#B0AAF6", 
               "size": 1200
             }, 
             "id": "Source/Trigonometry/TrigonometryTable", 
             "name": "Trig. Table"
           } 
           
         ], 
         "data": {
           "description": "Trigonometry Chapter", 
           "$color": "#DD3333", 
           "days": 1, 
           "$angularWidth": 4000, 
           "size": 186221
         }, 
         "id": "Source/Trigonometry", 
         "name": "Trigonometry"
       }
     ], 
     "data": {
       "$type": "none"
     }, 
     "id": "Source", 
     "name": "Grade 9 Mathematics"
   };
  
      //end
    //init Sunburst
    var sb = new $jit.Sunburst({
        //id container for the visualization
        injectInto: 'infovis',
        //Distance between levels
        levelDistance: 100,
        //Change node and edge styles such as
        //color, width and dimensions.
        Node: {
          overridable: true,
          type: useGradients? 'gradient-multipie' : 'multipie'

        },
        //Select canvas labels
        //'HTML', 'SVG' and 'Native' are possible options
        Label: {
          type: 'Native',
          size: 12,
          color: "#111",
          style:'bold'

        },
        //Change styles when hovering and clicking nodes
        NodeStyles: {
          enable: true,
          type: 'Native',
          stylesClick: {
            'color': '#B0AAF6'
          },
          stylesHover: {
            'color': '#3366FF'
          }
        },
        //Add tooltips
        Tips: {
          enable: true,
          onShow: function(tip, node) {
            var html = "<div class=\"tip-title\">" + node.name + "</div>"; 
            var data = node.data;
            if("days" in data) {
              html += "<b>Last modified:</b> " + data.days + " days ago";
            }
            if("size" in data) {
              html += "<br /><b>File size:</b> " + Math.round(data.size / 1024) + "KB";
            }
            tip.innerHTML = html;
          }
        },
        //implement event handlers
        Events: {
          enable: true,
          onClick: function(node) {
            if(!node) return;
            //Build detailed information about the file/folder
            //and place it in the right column.
            var html = "<h4>" + node.name + "</h4>", data = node.data;
            if("days" in data) {
              html += "<b>Last modified:</b> " + data.days + " days ago";
            }
            if("size" in data) {
              html += "<br /><br /><b>File size:</b> " + Math.round(data.size / 1024) + "KB";
            }
            if("description" in data) {
              html += "<br /><br /><b>Last commit was:</b><br /><pre>" + data.description + "</pre>";
            }
            $jit.id('inner-details').innerHTML = html;
            //hide tip
            sb.tips.hide();
            //rotate
            sb.rotate(node, animate? 'animate' : 'replot', {
              duration: 1000,
              transition: $jit.Trans.Quart.easeInOut
            });
          }
        },
        // Only used when Label type is 'HTML' or 'SVG'
        // Add text to the labels. 
        // This method is only triggered on label creation
        onCreateLabel: function(domElement, node){
          var labels = sb.config.Label.type,
              aw = node.getData('angularWidth');
          if (labels === 'HTML' && (node._depth < 2 || aw > 2000)) {
            domElement.innerHTML = node.name;
          } else if (labels === 'SVG' && (node._depth < 2 || aw > 2000)) {
            domElement.firstChild.appendChild(document.createTextNode(node.name));
          }
        },
        // Only used when Label type is 'HTML' or 'SVG'
        // Change node styles when labels are placed
        // or moved.
        onPlaceLabel: function(domElement, node){
          var labels = sb.config.Label.type;
          if (labels === 'SVG') {
            var fch = domElement.firstChild;
            var style = fch.style;
            style.display = '';
            style.cursor = 'pointer';
            style.fontSize = "0.8em";
            fch.setAttribute('fill', "#fff");
          } else if (labels === 'HTML') {
            var style = domElement.style;
            style.display = '';
            style.cursor = 'pointer';
            style.fontSize = "0.8em";
            style.color = "#ddd";
            var left = parseInt(style.left);
            var w = domElement.offsetWidth;
            style.left = (left - w / 2) + 'px';
          }
        }
   });
    //load JSON data.
    sb.loadJSON(param );
    //compute positions and plot.
    sb.refresh();
    //end
}
