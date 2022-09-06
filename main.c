#include <raylib.h>

int main() {
	InitWindow(800, 450, "Texture Balls");

	Camera3D camera = { 0 };
    camera.position = (Vector3){ 0.0f, 10.0f, 10.0f };  // Camera position
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };      // Camera looking at point
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };          // Camera up vector (rotation towards target)
    camera.fovy = 45.0f;                                // Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE;             // Camera mode type

    Vector3 sphere_position = { 0.0f, 0.0f, 0.0f };

    SetTargetFPS(60);   

	while (!WindowShouldClose()) {
		if (IsKeyDown('W')) sphere_position.z -= 3.0f;
		if (IsKeyDown('S')) sphere_position.z += 3.0f;
		if (IsKeyDown('A')) sphere_position.x += 3.0f;
		if (IsKeyDown('D')) sphere_position.x -= 3.0f;

		BeginDrawing();
			BeginMode3D(camera);
			ClearBackground(RAYWHITE);
			DrawSphere(sphere_position, 5, MAROON);
			EndMode3D();
		EndDrawing();
	}

	CloseWindow();

	return 0;
}