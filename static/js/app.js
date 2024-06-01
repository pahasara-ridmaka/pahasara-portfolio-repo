document.addEventListener("mousemove", function (e) {
  const follower = document.getElementById("follower");
  const mouseX = e.clientX;
  const mouseY = e.clientY;

  follower.style.transform = "translate3d(${mouseX}px, ${mouseY}px, 0)";
});
