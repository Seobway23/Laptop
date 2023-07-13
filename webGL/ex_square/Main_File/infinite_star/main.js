import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/examples/jsm/postprocessing/OutputPass.js';
import { GUI } from 'three/examples/jsm/libs/lil-gui.module.min.js';
import Stats from 'three/examples/jsm/libs/stats.module.js';

let camera,stats, scene, raycaster, renderer, control, clock, mixer, composer;
let mouse = new THREE.Vector2(), SELECTED;
let container = document.getElementById( 'myDIV' );

const params = {
    threshold: 0,
    strength: 1,
    radius: 0,
    exposure: 1
};

init();
animate();

function init() {
    stats = new Stats();
    container.appendChild( stats.dom );

    clock = new THREE.Clock();

    camera = new THREE.PerspectiveCamera( 70, container.clientWidth / container.clientHeight, 1, 10000 );
    camera.position.set( 0, 8, 8 );
    
    // camera = new THREE.PerspectiveCamera( 40, window.innerWidth / window.innerHeight, 1, 100 );
    // camera.position.set( - 5, 2.5, - 3.5 );
    
    scene = new THREE.Scene();
    scene.background = new THREE.Color('black');
    // scene.add(camera);

    let geometry = new THREE.BoxGeometry( 20, 20, 20 );

    
    for ( let i = 0; i < 1000; i ++ ) 
    {
        let geometry = new THREE.SphereGeometry(0.3,32,16);
        let material = new THREE.MeshBasicMaterial({color: 'white'});
        let sphere = new THREE.Mesh(geometry, material);
            
        
        sphere.position.x = Math.random() * 800 - 400;
        sphere.position.y = Math.random() * 800 - 400;
        sphere.position.z = Math.random() * 800 - 400;
        sphere.rotation.x = Math.random() * 2 * Math.PI;
        sphere.rotation.y = Math.random() * 2 * Math.PI;
        sphere.rotation.z = Math.random() * 2 * Math.PI;
        scene.add( sphere );
    }
    
    renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setClearColor( 0xf0f0f0 );
    renderer.setPixelRatio( container.devicePixelRatio );
    renderer.setSize( container.clientWidth, container.clientHeight );
    renderer.useLegacyLights = false;

    
    // renderer.sortObjects = false;

    container.appendChild( renderer.domElement );
    
    control = new OrbitControls( camera, renderer.domElement );
    // control.update();
    control.maxPolarAngle = Math.PI * 0.5;
    control.minDistance = 3;
    control.maxDistance = 8;

    scene.add( new THREE.AmbientLight( 0xcccccc ) );
    const pointLight = new THREE.PointLight( 0xffffff, 100 );
    camera.add( pointLight );
    
    const renderScene = new RenderPass( scene, camera );
    const bloomPass = new UnrealBloomPass( new THREE.Vector2( window.innerWidth, window.innerHeight ), 1.5, 0.4, 0.85 );
    bloomPass.threshold = params.threshold;
    bloomPass.strength = params.strength;
    bloomPass.radius = params.radius;
    
    const outputPass = new OutputPass( THREE.ReinhardToneMapping );
    
    composer = new EffectComposer( renderer );
    composer.addPass( renderScene );
    composer.addPass( bloomPass );
    composer.addPass( outputPass );
    
    const loader = new GLTFLoader();
    loader.load(
        'models/abcd.gltf', ( gltf ) => {
        const model = gltf.scene;

        scene.add(model);   

        animate();
    } );
        // scene.add( gltf.scene );

        // render();



    const gui = new GUI();

    const bloomFolder = gui.addFolder( 'bloom' );

    bloomPass.threshold = Number( 0 );

    bloomFolder.add( params, 'threshold', 0.0, 1.0 ).onChange( function ( value ) {

        bloomPass.threshold = Number( value );

    } );

    bloomPass.strength = Number( 0.6 );

    bloomFolder.add( params, 'strength', 0.0, 3.0 ).onChange( function ( value ) {

        bloomPass.strength = Number( value );

    } );

    bloomPass.radius = Number( 0.1 );

    gui.add( params, 'radius', 0.0, 1.0 ).step( 0.01 ).onChange( function ( value ) {

        bloomPass.radius = Number( value );

    } );

    const toneMappingFolder = gui.addFolder( 'tone mapping' );

    outputPass.toneMappingExposure = Math.pow( 1.3, 4.0 );

    toneMappingFolder.add( params, 'exposure', 0.1, 2 ).onChange( function ( value ) {

        outputPass.toneMappingExposure = Math.pow( value, 4.0 );

    } );

    // raycaster = new THREE.Raycaster();
    
    container.addEventListener( 'mousemove', onDocumentMouseMove, false );
    container.addEventListener( 'mousedown', onDocumentMouseDown, false );
    container.addEventListener( 'resize', onresize, false );
    
    window.addEventListener( 'resize', onWindowResize );

}
function onDocumentMouseMove( event ) {
    event.preventDefault();

    let gapX = event.clientX - event.offsetX;
    let gapY = event.clientY - event.offsetY;
    
    mouse.x = ((event.clientX - gapX)/( container.clientWidth )) * 2 - 1;
    mouse.y = -((event.clientY - gapY)/( container.clientHeight )) * 2 + 1;

}
        
function onDocumentMouseDown( event ) {
    console.log(1)
    // event.preventDefault();
    if ( SELECTED )
    {
        // SELECTED.currentHex = 0x00ff00 * Math.random();
        // SELECTED.material.emissive.setHex( SELECTED.currentHex );
    }

}
function render() {
    // find intersections
    raycaster.setFromCamera( mouse, camera );

    let intersects = raycaster.intersectObjects( scene.children );

    if ( intersects.length > 0 ) {
        if ( SELECTED != intersects[0].object ) 
        {

            // if ( SELECTED ) SELECTED.material.emissive.setHex( SELECTED.currentHex );

            SELECTED = intersects[0].object;
            SELECTED.currentHex = SELECTED.material.emissive.getHex();
            SELECTED.material.emissive.setHex( 0xff0000 );
            container.style.cursor = 'pointer';

        }
    } 
    else 
    {
        if ( SELECTED ) 
        {
            // SELECTED.material.emissive.setHex( SELECTED.currentHex );
            SELECTED = null;
            container.style.cursor = 'auto';
        }
    }

    renderer.render( scene, camera );

}
function onWindowResize() {

    const width = window.innerWidth;
    const height = window.innerHeight;

    camera.aspect = width / height;
    camera.updateProjectionMatrix();

    renderer.setSize( width, height );
    composer.setSize( width, height );

}

function animate() {
    requestAnimationFrame( animate );

    stats.update();

    composer.render();
}
