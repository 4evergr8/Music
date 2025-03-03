var photosController = new TKPageSliderController({
  id: 'photos',
  previousPageButton : '#photos .left-arrow',
  nextPageButton :     '#photos .right-arrow',
  
  backButton: '#photos .home',
  
  activatesFocusedPage : false,
  
  outlets : [  
	 { selector: '#photos .left-arrow',  name: 'btnLeftArrow' },
	 { selector: '#photos .right-arrow', name: 'btnRightArrow' }
  ]
});

photosController.slidingView.handleClick = function(event){
	
};

photosController.viewDidLoad = function () {
  this.slidingViewData = {
    orientation: TKSlidingViewOrientationHorizontal,
    activeElementIndex: 0,
    sideElementsVisible: 0,
    distanceBetweenElements: 0,
    sideOffsetBefore: 0,
    sideOffsetAfter: 0,
    elements: this.createPhotos(),
    incrementalLoading : false
  };

  this.pageControlData = {
    numPages: appData.numberOfPhotos,
    distanceBetweenPageIndicators: 62,
    showPageElements: false,
    indicatorElement: { type: "emptyDiv" },
    pageElement: { type: "emptyDiv" },
    incrementalJumpsOnly: false,
    allowsDragging: true
  };
};

photosController.createPhotos = function () {
  var elements = [];
  for (var i = 1; i <= appData.numberOfPhotos; i++) {
    var padded_index = (i < 10) ? '0' + i : i;
    var url = 'images/photos/ph_' + padded_index + '.jpg';
    elements.push({ 
      type: 'container',
      children: [ {type: 'image', src: url } ]
    });
  }
  return elements;
};
