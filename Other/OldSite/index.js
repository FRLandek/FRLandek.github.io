import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.127.0/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.127.0/examples/jsm/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#bg'),
    alpha:true
});

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.setZ(20);

//scene.background = new THREE.Color(0xffffff);

//---------------------------------------------------------------------

const meshConfigs = [
    {
      path: '/models/peachs_castle.glb',
      position: { x: 15, y: -2, z: 0 },
      speed: .005,
      game: "Super Mario 64 (Nintendo)",
      creator: "Nintendo"
    },
    {
      path: '/models/skull.glb',
      position: { x: 5, y: 1, z: 15 },
      speed: .05,
      game: "None",
      creator: "soidev (Sketchfab)"
    },
    {
      path: '/models/companion_cube.glb',
      position: { x: 5, y: 0.5, z: 15 },
      speed: .005,
      game: "Portal (Valve)",
      creator: "Michael Klement (Sketchfab)"
    },
    {
      path: '/models/wheatley.glb',
      position: { x: 40, y: 8, z: -30 },
      speed: .005,
      game: "Portal 2 (Valve)",
      creator: "Valve"
    },
    {
      path: '/models/bloxy_cola.glb',
      position: { x: 7, y: 1, z: 13 },
      speed: .005,
      game: "Roblox",
      creator: "Roblox"
    },
    {
      path: '/models/normal.glb',
      position: { x: 6, y: 1, z: 13 },
      speed: .005,
      game: "Geometry Dash (Robtop)",
      creator: "Khalfanel (Sketchfab)",
    },
    {
      path: '/models/chimpanzini_bananini.glb',
      position: { x: 2, y: 0, z: 17 },
      speed: .1,
      game: "None",
      creator: "Aizenx. (Sketchfab)"
    }
  ];
  

//random picks a mesh
const config = meshConfigs[Math.floor(Math.random() * meshConfigs.length)];

const loader = new GLTFLoader();

// Load your model (relative path or from a server)
let loadedModel;

loader.load(config.path, (gltf) => {
    loadedModel = gltf.scene;

    loadedModel.position.set(config.position.x, config.position.y, config.position.z);

    scene.add(loadedModel);
    document.getElementById("gameName").textContent = `Game: ${config.game}`;
    document.getElementById("creatorName").textContent = `Model by: ${config.creator}`;

});


const ambientLight = new THREE.AmbientLight(0xffffff); //lights up entire scene

scene.add(ambientLight)

//loadedmodel.position.set(25,0,0)


function animate() {
    requestAnimationFrame(animate);

    loadedModel.rotation.y += config.speed;

    renderer.render(scene, camera);
}
animate();