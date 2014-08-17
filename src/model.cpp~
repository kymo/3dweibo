/*
 * Name: glut.cpp
 * Desc: None
 * Time: 2014-08-14
 */


#include <gl/glut.h>
#include <map>
#include <vector>
#include <windows.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <time.h>
#include <string>

using namespace std;
#define LEN 1024
typedef struct person
{
	string name;	//
	string text;	// 
	float weight;	// quanzhong
}Person;

typedef struct ball
{
	float x,y,z;
	float r,g,b;
	float size;
	string text;
	string name;
}Ball;

typedef struct line
{
	float x0, y0, z0;
	float x1, y1, z1;
	float r, g ,b;
}Line;


int x;
float mouse_x, mouse_y;
float wx,wy,wz;
vector<Line> lines;
vector<Person> persons;
vector<Ball> balls;



void init_light()
{
	GLfloat light_ambient[] = { 0.0 , 0.0 , 1.0 , 100.0 };
	GLfloat light_diffuse[] = { 1.0 , 1.0 , 1.0 , 100.0 };
	//指定光源的位置
	GLfloat light_position[] = { 0 , 0, 400 , 1.0 };
 
	//用定义好的光源属性给指定光源GL_LIGHT0进行设置

	glLightfv(GL_LIGHT0 , GL_AMBIENT , light_ambient);
	glLightfv(GL_LIGHT0 , GL_DIFFUSE , light_diffuse);
	glLightfv(GL_LIGHT0 , GL_POSITION , light_position);


	
	GLfloat light_position1[] = { 0 , 0, -400 , 1.0 };
	
	glLightfv(GL_LIGHT1 , GL_AMBIENT , light_ambient);
	glLightfv(GL_LIGHT1 , GL_DIFFUSE , light_diffuse);
	glLightfv(GL_LIGHT1 , GL_POSITION , light_position1);

	
	GLfloat light_position2[] = { 400 , 0, 0 , 1.0 };
	
	glLightfv(GL_LIGHT2 , GL_AMBIENT , light_ambient);
	glLightfv(GL_LIGHT2 , GL_DIFFUSE , light_diffuse);
	glLightfv(GL_LIGHT2 , GL_POSITION , light_position2);

	GLfloat light_position3[] = { -400 , 0, 0 , 1.0 };
	
	glLightfv(GL_LIGHT3 , GL_AMBIENT , light_ambient);
	glLightfv(GL_LIGHT3 , GL_DIFFUSE , light_diffuse);
	glLightfv(GL_LIGHT3 , GL_POSITION , light_position3);


}
void init (void)
{
	glClearColor (0.0, 0.0, 0.0, 1.0);
	glMatrixMode (GL_PROJECTION);
	glOrtho (-800.0, 800.0, -800, 800.0, -800, 800); //设置显示的范围是X:-5.0~5.0, Y:-5.0~5.0
	glMatrixMode (GL_MODELVIEW);
}

void drawSquare() //绘制中心在原点，边长为2的正方形
{
	glPushMatrix();
	glBegin (GL_LINES);
		glVertex3f(10,10,10);
		glVertex3f(20,20,20);
		glVertex3f(100,200,300);
	glEnd ( );
	glPopMatrix();
}


void draw_ball(GLfloat x, GLfloat y, GLfloat z, 
	GLfloat a, GLfloat c, GLfloat d,
	GLfloat r, GLfloat g, GLfloat b)
{
	glPushMatrix();
	glTranslatef( x,y,z);
		glColor3f(r,g,b);
		glutSolidSphere(a, c, d);
	glPopMatrix();

}

void drawCNString(const char* str)
{
    int len, i;
    wchar_t* wstring;
    HDC hDC = wglGetCurrentDC(); //获取显示设备
    GLuint list = glGenLists(1); //申请1个显示列表
    //计算字符的个数
    //如果是双字节字符的（比如中文字符），两个字节才算一个字符
    //否则一个字节算一个字符
    len = 0;
    for(i=0; str[i]!='\0'; ++i)
    {
        if( IsDBCSLeadByte(str[i]) )
            ++i;
        ++len;
    }
    // 将混合字符转化为宽字符
    wstring = (wchar_t*)malloc((len+1) * sizeof(wchar_t));
    MultiByteToWideChar(CP_ACP, MB_PRECOMPOSED, str, -1, wstring, len);
    wstring[len] = L'\0';// 只是转义符,它本身的类型是wchar_t
    // 逐个输出字符
    for(i=0; i<len; ++i)
    {
    wglUseFontBitmapsW(hDC, wstring[i], 1, list);
    glCallList(list);
    }
    // 回收所有临时资源
    free(wstring);
    glDeleteLists(list, 1);
}

void draw_line(GLfloat x0, GLfloat y0, GLfloat z0,
	GLfloat x1, GLfloat y1, GLfloat z1)
{
	/*
	glColor3f(0.5f,0.5f,0.5f);
	glBegin(GL_LINES);
		glLineWidth(0.4);
		glVertex3f(x0,y0,z0);
		glVertex3f(x1,y1,z1);
	glEnd();
	*/
}

void myDraw1 (void)

{

	glClear (GL_COLOR_BUFFER_BIT); //清空

	init_light();
	glEnable(GL_LIGHTING);
	//开启设置的光源GL_LIGHT0
	/*glEnable(GL_LIGHT0);
	*/

	glEnable(GL_LIGHT0);
	glEnable(GL_LIGHT1);
	glEnable(GL_LIGHT2);
	glEnable(GL_LIGHT3);
	glEnable(GL_COLOR_MATERIAL);
	GLfloat gAmbient[] = {0.6, 0,6, 0,6, 1.0};
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, gAmbient);


	draw_ball(200,0,0,10,1000,1000, 1.0,0,0);
	
	for(int i = 0;i < balls.size(); i ++)
	{

		
		glRasterPos3f(balls[i].x, balls[i].y, balls[i].z);
		drawCNString(balls[i].name.c_str());
		draw_ball(balls[i].x, balls[i].y, balls[i].z,
			balls[i].size, 1000, 1000,
			balls[i].r, balls[i].g, balls[i].b);
	}

	for(int i = 0; i < lines.size(); i ++) {
		draw_line ( lines[i].x0, lines[i].y0, lines[i].z0,
			lines[i].x1, lines[i].y1, lines[i].z1);
	}
	glFlush ( );

}

void myDraw2 (void)

{
	glClear (GL_COLOR_BUFFER_BIT); //清空

	glLoadIdentity(); //将当前矩阵设为单位矩阵

	glColor3f (1.0, 0.0, 0.0);

	drawSquare(); //在原点处绘制边长为2红色正方形

	glPushMatrix();
	glTranslatef(2.0,3.0,0.0); //向右移动2单位，向上移动3单位
	glColor3f (0.0, 1.0, 0.0);
	drawSquare(); //绘制边长为2绿色正方形
	glPopMatrix();
	glTranslatef(2.0,0.0,0.0); //再向右移动2单位
	glColor3f (0.0, 0.0, 1.0);
	drawSquare(); //绘制边长为2蓝色正方形
	glFlush ( );
}


void mouse(int button, int state, int x, int y)
{
	/*GLint hits;*/
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) 
	{
		glRotatef(10,0,1,0);
		glutPostRedisplay();
	}

	if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN) 
	{
		glScalef(1.1,1.1,1.1);
		glutPostRedisplay();
	}

} 

void motion(int x, int y)
{
	GLdouble modelview[16];
	GLdouble projection[16];
	GLint viewport[4];
	glGetDoublev (GL_MODELVIEW_MATRIX, modelview);
	glGetDoublev (GL_PROJECTION_MATRIX, projection);
	glGetIntegerv (GL_VIEWPORT, viewport); GLdouble world_x, world_y, world_z; // 获取近裁剪面上的交点
	gluUnProject( (GLdouble) x, (GLdouble)y, 0.0, 
	modelview, projection, viewport, 
	&world_x, &world_y, &world_z); 
	gluUnProject( (GLdouble) x, (GLdouble) y, 1.0, 
	modelview, projection, viewport, 
	&world_x, &world_y, &world_z); 

}

bool cmp(const Person a, const Person b) {
	return a.weight < b.weight;
}

void myAnimate()
{
	
	glRotatef(5, 0, 1,0); 

	draw_ball(x,0,0, 10, 300,300, 0.0, 1.0, 0.0);
	x += 10;
	glutPostRedisplay();
}

void read_file(const char *file)
{
	ifstream is(file);
	string line;
	float max = 0.0;
	while(getline(is, line)) {
		Person temp_person;
		char str[2048];
		strcpy(str, line.c_str());
		char *name = strtok(str, "\t");
		char *text = strtok(NULL, "\t");
		strtok(NULL, "\t");
		char *weight = strtok(NULL, "\t");
		temp_person.name = string(name);
		temp_person.text = string(text);
		temp_person.weight = atof(weight);
		persons.push_back(temp_person);
		if(max < temp_person.weight)
			max = temp_person.weight;
	}
	//sort(persons.begin(), persons.end(), cmp);
	float x, y ,z;
	x = y = z = 0.0;
	x = 200;
	y = 0;
	z = 0;
	srand((unsigned)time(NULL)); 
	float r, g, b;
	r = 0.1;
	g = 0.1;
	b = 0.1;
	

	for (int i = 0; i < persons.size(); i ++) {

		int t=  rand() % 7;
			Ball t_ball; 
			float t_x,t_y,t_z;
		if(t != 6) {
			t_x = x + rand() % 300 - 150;
			t_y = y + (rand() % 300 - 150);
			t_z = z + (rand() % 300 - 150);
			t_ball.x = t_x;
			t_ball.y = t_y;
			t_ball.z = t_z;
			
			Line t_line;
			t_line.x0 = 200, t_line.x1 = t_x;
			t_line.y0 = 0, t_line.y1 = t_y;
			t_line.z0 = 0, t_line.z1 = t_z;
			lines.push_back(t_line);
		}
		else
		{
			x=t_x,y=t_y,z=t_z;
		}
		t_ball.r = r + (rand() % 10 - 5) * 1.0 * i / 100 ;
		t_ball.g = g + (rand() % 10 - 5) * 1.0 * i / 100 ;
		t_ball.b = b + (rand() % 10 - 5) * 1.0 * i / 100 ;
		if(persons[i].weight < 10000)
			t_ball.size = 5;
		else if(persons[i].weight < 20000)
			t_ball.size = 8;
		else if(persons[i].weight < 50000)
			t_ball.size = 10;
		else if(persons[i].weight < 100000)
			t_ball.size = 12;
		else
			t_ball.size = 15;
		t_ball.name = persons[i].name;
		t_ball.text = persons[i].text;
		balls.push_back(t_ball);
	}
}

void main (int argc, char** argv)

{

	glutInit (&argc, argv);

	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

	glutInitWindowPosition (0, 0);

	glutInitWindowSize (800, 800);

	glutCreateWindow ("Translate函数示例");

	init();
	read_file("friends_list.txt");

	glutDisplayFunc (myDraw1);
	glutMouseFunc(mouse);
	//glutIdleFunc(myAnimate);//设置全局空闲回调函数 
	glutMotionFunc(motion);
	glutMainLoop ( );

}