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

        const particles = [];
        this._particles = particles;

		this._setupCamera();
		this._setupLight();
		this._setupModel();
		this._setControls();
        this._update_position();

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
		camera.position.z = 10;
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

	// _setupModel() {
	// 	const geometry = new THREE.S(1, 1, 1);
	// 	const fillmaterial = new THREE.MeshPhongMaterial({ color: 0x44a88  });
	// 	const cube = new THREE.Mesh(geometry, fillmaterial);
	// 	// const cube = new THREE.Mesh(geometry, material);
		
	// 	const lineMaterial = new THREE.LineBasicMaterial({color: 0x44a88 });
	// 	const line = new THREE.LineSegments(
	// 		new THREE.WireframeGeometry(geometry), lineMaterial,
	// 	)

	// 	this._scene.add(cube);
	// 	this._cube = cube;
	// }

    // // setcontorl 초기
	// _setControls() {
	// 	new OrbitControls(this._camera, this._divContainer);
	// }


// 수정
    _setControls() {
        const controls = new OrbitControls(this._camera, this._divContainer);

        this._divContainer.addEventListener('change', this._handleControlsChange.bind(this));
        this._divContainer.addEventListener('click', this._handleSphereClick.bind(this));
        this._controls = controls;
        

    }
    _handleControlsChange() {
        // 필요한 경우 처리할 로직 추가
    }
    
    _handleSphereClick(event) {
        event.preventDefault();
        
        this._raycaster.setFromCamera({ x: 0, y: 0 }, this._camera);
        
        // console.log(this._raycaster)
        const intersects = this._raycaster.intersectObjects(this._particles);
    
        if (intersects.length > 0) {
            // 클릭한 별에게 접근 가능, 
            console.log('intersects:' , intersects[0].object.position);
            
        }
    }
    
// 수정
    _setupModel() {
	let particle, material;

	for (let zpos = -1000; zpos < 1000; zpos += 20) {
		const color = new THREE.Color(Math.random() * 0xffffff);

		material = new THREE.MeshBasicMaterial({ color: color });

		const geometry = new THREE.SphereGeometry(5, 16, 16);

		particle = new THREE.Mesh(geometry, material);
        console.log(particle)
		particle.position.x = Math.random() * 1000 - 500;
		particle.position.y = Math.random() * 1000 - 500;
		particle.position.z = zpos;

		this._scene.add(particle);
		this._particles.push(particle);
		
		console.log('this_particless:',this._particles)

		// particles의 갯수가 2개 이상일 때
		if ( this._particles.length > 1 & this._particles.length < 10) {
			// 선의 시작과 끝 점 
			const startPoint = this._particles[this._particles.length-1].position
			const endPoint = this._particles[this._particles.length-2].position

			console.log(this._particles[-1])
			// const endPoint = new THREE.Vector3(1, 0, 0);
			
			console.log( 'startPoint:', startPoint)
			console.log( 'endpoint:' , endPoint)
			// 선의 지오메트리 생성
			const linegeometry = new THREE.BufferGeometry().setFromPoints([startPoint, endPoint]);
			
			// 선의 metrial 생성
			const lineMaterial = new THREE.LineBasicMaterial({
				color: 0xffff00,
				linewidth: 5,
				emissive: 0xffffff, // Set a brighter emissive color
				specular: 0xffffff, // Set a brighter specular color
				shininess: 100,
			})
			// 선 생성
			const line = new THREE.Line(linegeometry, lineMaterial);
			this._scene.add(line);
			line.material.color.convertSRGBToLinear().multiplyScalar(2);
			console.log('line:', line)


		}
	}

    const zero_color = new THREE.Color(Math.random() * 0xffffff);
    const zero_material = new THREE.MeshBasicMaterial({color: zero_color});
    const zero_geometry = new THREE.SphereGeometry(10, 32, 32);
    const zero_particle = new THREE.Mesh(zero_geometry, zero_material);
    zero_particle.position.x = 0
    zero_particle.position.y = 0
    zero_particle.position.z = 0
    this._scene.add(zero_particle)
    this._particles.push(zero_particle)
    }

// updateParticles() {
// 	for (let i = 0; i < particles.length; i++) {
// 		const particle = particles[i];
// 		particle.position.z += mouseY * 0.1;

// 		if (particle.position.z > 1000) particle.position.z -= 2000;
//         }
//     }

            


    //         // material = new THREE.MeshBasicMaterial({color: 0xffffff});
    //         particle = new THREE.Mesh(geometry, material);

    //         particle.position.x = 1;
    //         particle.position.y = 1;
    //         particle.position.z = 1;

    //         this._scene.add(particle);
    //         this._particle = particle;
    //         console.log(particle);
    // }
    

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
        for (let i = 0; i < this._particles.length; i++) {
            const particle = this._particles[i];
            particle.rotation.y = time;
            particle.rotation.z = time;
	    }
    }

    _update_position() {
        for (let i = 0; i < this._particles.length; i++) {
            const particle = this._particles[i];
            console.log('x:', particle.position.x, 'y:', particle.position.y, 'z:', particle.position.z);
        }
    }
    
}

window.onload = function () {
	new App();
};