
AOS.init();

AOS.init({
  
  offset: 120, // offset (in px) from the original trigger point
  delay: 0, // values from 0 to 3000, with step 50ms
  duration: 700, // values from 0 to 3000, with step 50ms
  easing: 'ease', // default easing for AOS animations
  once: false, // whether animation should happen only once - while scrolling down
  mirror: false, // whether elements should animate out while scrolling past them
  anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation

});

window.addEventListener('load', () => {
    const tabContent = document.getElementById('interestsTabContent');
    const tabs = tabContent.querySelectorAll('.tab-pane');
    let maxHeight = 0;

    tabs.forEach(tab => {
        tab.style.display = 'block'; // temporarily show to measure
        const height = tab.offsetHeight;
        if (height > maxHeight) maxHeight = height;
        tab.style.display = ''; // reset
    });

    tabContent.style.minHeight = maxHeight + 'px';
});