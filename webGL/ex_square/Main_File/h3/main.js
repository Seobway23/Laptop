import * as THREE from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

class App {
	constructor() {
		const divContainer = document.querySelector("#webgl-container");
		this._divContainer = divContainer;

		const renderer = new THREE.WebGLRenderer({ antialias: true });
		renderer.setPixelRatio(window.devicePixelRatio);
		divContainer.appendChild(renderer.domElement);
		this._renderer = renderer;

		const scene = new THREE.Scene();
		this._scene = scene;

		this._setupCamera();
		this._setupLight();
		this._setupModel();
		this._setControls();
        // this._update_position();

		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));

        // raycaster 초기화
        this._raycaster = new THREE.Raycaster();
	}

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 100000);
		camera.position.z = 3;
        camera.lookAt(new THREE.Vector3(0, 0, 0)); // 원하는 방향으로 설정
		this._camera = camera;

	}

	_setupLight() {
		const color = 0xffffff;
		const intensity = 1;
		const light = new THREE.DirectionalLight(color, intensity);
		light.position.set(-1, 2, 4);
		this._scene.add(light);
	}

	_setupModel() {
		const material = new THREE.MeshPhongMaterial({ 
            visible: true,
			transparent: true,
			opacity: 0.5,
			// transparent true -> opacity 설정 가능
			// depthTest: true,
			// deptWrite: true,
			side: THREE.FrontSide,
			// side: THREE.DoubleSide,

			// 빛 효과
			emissive: 0x000000,
			specular: 0xffff00,
			shininess: 10,
			flatShading: true,
			
			// 메탈 효과
			// roughness : 1,
			// metalness: 0.5,

			// 코팅
			// clearcoat: 1,
			// clearcoatRoughness: 0,
			
			color: 0xff0000,
            wireframe: false
        });

        const box = new THREE.Mesh(new THREE.BoxGeometry(1,1,1), material)
        box.position.set(-1,0,0)
        this._scene.add(box)

        const sphere = new THREE.Mesh(new THREE.SphereGeometry(0.7, 32, 32), material)
        sphere.position.set(1,0,0)
        this._scene.add(sphere)
		
		// 선의 시작과 끝 점 
		console.log(box.position)
		const startPoint = box.position
		const endPoint = sphere.position
		// const endPoint = new THREE.Vector3(1, 0, 0);
	
		// 선의 지오메트리 생성
		const geometry = new THREE.BufferGeometry().setFromPoints([startPoint, endPoint]);
		
		// 선의 metrial 생성
		const lineMaterial = new THREE.LineBasicMaterial({
			color: 0xffff00,
			linewidth:5,
			emissive: 0xffffff, // Set a brighter emissive color
			specular: 0xffffff, // Set a brighter specular color
			shininess: 100,
		})
		// 선 생성
		const line = new THREE.Line(geometry, lineMaterial);
		this._scene.add(line);



	}

    // setcontorl 초기
	_setControls() {
		const controls = new OrbitControls(this._camera, this._divContainer);
		this._controls = controls;

	}


// 수정
    _setControls() {
        const controls = new OrbitControls(this._camera, this._divContainer);
        // this._divContainer.addEventListener('change', this._handleControlsChange.bind(this));
        // this._divContainer.addEventListener('click', this._handleSphereClick.bind(this));
        this._controls = controls;
        

    }
    // _handleControlsChange() {
    //     // 필요한 경우 처리할 로직 추가
    // }
    
    // _handleSphereClick(event) {
    //     event.preventDefault();
        
    //     this._raycaster.setFromCamera({ x: 0, y: 0 }, this._camera);
        
    //     // console.log(this._raycaster)
    //     const intersects = this._raycaster.intersectObject(this._particle);
    
    //     if (intersects.length > 0) {
    //         // 클릭한 별에게 접근 가능, 
    //         console.log('intersects:' , intersects[0].object.position);
    //         const targetUrl = 'h1/index.html'
    //         window.location.href = targetUrl;
    //     }
    // }
    
// 수정

	resize() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;

		this._camera.aspect = width / height;
		this._camera.updateProjectionMatrix();

		this._renderer.setSize(width, height);
	}

	render(time) {
		this._renderer.render(this._scene, this._camera);
		this.update(time);
		requestAnimationFrame(this.render.bind(this));
	}
    
	update(time) {
		time *= 0.0001; // secondunit
		// this._cube.rotation.x = time;
		// this._particle.rotation.y = time;
		// this._particle.rotation.z = time;
        // console.log(this._particle)
	}

    // _update_position() {
    //     console.log('x: ',this._particle.position.x,'   ','y:',this._particle.position.y)
        
    // }
}

window.onload = function () {
	new App();
};