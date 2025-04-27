import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.127.0/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.127.0/examples/jsm/controls/OrbitControls.js';


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#bg')
});

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.setZ(30);

const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
const material = new THREE.MeshStandardMaterial({ color: 0xFF6347}); //StandardMaterial interacts with light, use basic material for  
const torus = new THREE.Mesh(geometry, material);                    //non light interactions

scene.add(torus);

const pointLight = new THREE.PointLight(0xffffff) //lightbulb type light
pointLight.position.set(5,5,5)

const ambientLight = new THREE.AmbientLight(0xffffff); //lights up entire scene

scene.add(pointLight, ambientLight)


const lightHelper = new THREE.PointLightHelper(pointLight) //shows where the light is
const gridHelper = new THREE.GridHelper(200, 50);
scene.add(lightHelper, gridHelper)

const controls = new OrbitControls(camera, renderer.domElement);

//--------------------------------------------------------------------------------------------------
//function declaration
function addStar() {
    const geometry = new THREE.SphereGeometry(0.25, 24, 24)
    const material = new THREE.MeshStandardMaterial( {color: 0xffffff })
    const star = new THREE.Mesh( geometry, material);
    
    const [x, y, z] = Array(3).fill().map(() => THREE.MathUtils.randFloatSpread( 100 ) ); //random array of stars

    star.position.set(x, y, z);
    scene.add(star)
}

Array(200).fill().forEach(addStar) //places 200 stars
//--------------------------------------------------------------------------------------------------

const spaceTexture = new THREE.TextureLoader().load('space.jpg')
scene.background = spaceTexture;


const moonTexture = new THREE.TextureLoader().load('moon.jpg')
const normalTexture = new THREE.TextureLoader().load('normal.jpg')

const moon = new THREE.Mesh(
    new THREE.SphereGeometry(3, 32, 32),
    new THREE.MeshStandardMaterial( {
        map: moonTexture,
        normalMap: normalTexture //normal maps make textures look bumpy
    } )
);

scene.add(moon)

function animate() {
    requestAnimationFrame(animate);

    torus.rotation.x += 0.01;
    torus.rotation.y += 0.005;
    torus.rotation.z += 0.01;

    controls.update();

    renderer.render(scene, camera);
}
animate();
