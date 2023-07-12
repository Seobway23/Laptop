import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

let camera, scene, raycaster, renderer, light, control;
let mouse = new THREE.Vector2(), SELECTED;
let radius = 100, theta = 0;
let container = document.getElementById( 'myDIV' );

init();
animate();

function init() {
        
        camera = new THREE.PerspectiveCamera( 70, container.clientWidth / container.clientHeight, 1, 10000 );
        camera.position.set( 0, 20, 100 );
        
        scene = new THREE.Scene();
        
        light = new THREE.DirectionalLight( 0xffffff, 1 );
        light.position.set( 1, 1, 1 ).normalize();
        scene.add( light );

        let geometry = new THREE.BoxGeometry( 20, 20, 20 );

        for ( let i = 0; i < 1000; i ++ ) 
        {
            let grey = Math.random();
            let object = new THREE.Mesh( 
                geometry, 
                new THREE.MeshLambertMaterial({ 
                    color: new THREE.Color( grey, grey , grey )  
                })
            );

            object.position.x = Math.random() * 800 - 400;
            object.position.y = Math.random() * 800 - 400;
            object.position.z = Math.random() * 800 - 400;
            object.rotation.x = Math.random() * 2 * Math.PI;
            object.rotation.y = Math.random() * 2 * Math.PI;
            object.rotation.z = Math.random() * 2 * Math.PI;
            object.scale.x = Math.random() + 0.5;
            object.scale.y = Math.random() + 0.5;
            object.scale.z = Math.random() + 0.5;
            scene.add( object );
        }

        renderer = new THREE.WebGLRenderer();
        renderer.setClearColor( 0xf0f0f0 );
        renderer.setPixelRatio( container.devicePixelRatio );
        renderer.setSize( container.clientWidth, container.clientHeight );

        // renderer.sortObjects = false;

        container.appendChild( renderer.domElement );
		
        control = new OrbitControls( camera, renderer.domElement );
        control.update();

        raycaster = new THREE.Raycaster();

        container.addEventListener( 'mousemove', onDocumentMouseMove, false );
        container.addEventListener( 'mousedown', onDocumentMouseDown, false );
        container.addEventListener( 'resize', onresize, false );

    }
    function onDocumentMouseMove( event ) {

        event.preventDefault();

        let gapX = event.clientX - event.offsetX;
        let gapY = event.clientY - event.offsetY;
        
        mouse.x = ((event.clientX - gapX)/( container.clientWidth )) * 2 - 1;
        mouse.y = -((event.clientY - gapY)/( container.clientHeight )) * 2 + 1;

    }
            
    function onDocumentMouseDown( event ) {

        event.preventDefault();
        if ( SELECTED )
        {
            SELECTED.currentHex = 0x00ff00 * Math.random();
            SELECTED.material.emissive.setHex( SELECTED.currentHex );
        }

    }
    function render() {
        // find intersections
        raycaster.setFromCamera( mouse, camera );

        let intersects = raycaster.intersectObjects( scene.children );

        if ( intersects.length > 0 ) {
            if ( SELECTED != intersects[0].object ) 
            {

                if ( SELECTED ) SELECTED.material.emissive.setHex( SELECTED.currentHex );

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
                SELECTED.material.emissive.setHex( SELECTED.currentHex );
                SELECTED = null;
                container.style.cursor = 'auto';
            }
        }

        renderer.render( scene, camera );

    }
    

function animate() {
        requestAnimationFrame( animate );
        control.update();
        render();
  }