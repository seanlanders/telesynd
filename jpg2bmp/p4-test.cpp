#define p4_width 75
#define p4_height 75
static char p4_bits[] = {
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0xff,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xf0,0xff,
0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xfc,0xff,0xff,0x01,0x00,0x00,0x00,
0x00,0x00,0x00,0xfe,0xff,0xff,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xff,
0xff,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xff,0xff,0x0f,0x00,0x00,0x00,
0x00,0x00,0x00,0xff,0xff,0xff,0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0xfe,0xff,
0xff,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0xfc,0xff,0xff,0x1f,0x00,0x00,0x00,
0x00,0x00,0x00,0xfc,0xff,0xff,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0xfc,0xff,
0xff,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0xfe,0xff,0xff,0x3f,0x00,0x00,0x00,
0x00,0x00,0x00,0xfe,0xff,0xff,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0xfc,0xff,
0xff,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0xfc,0xff,0xff,0x7f,0x00,0x00,0x00,
0x00,0x00,0x00,0xfe,0xff,0xff,0x7f,0x00,0x00,0x00,0x00,0x00,0x00,0xe6,0xff,
0xff,0x7f,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xe3,0x7f,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0xfe,0x83,0x7f,0x00,0x00,0x00,0x00,0x00,0x00,0x38,0xfc,
0xff,0x7f,0x08,0x00,0x00,0x00,0x00,0x00,0x7c,0xf8,0xff,0x7f,0x08,0x00,0x00,
0x00,0x00,0x00,0x00,0xf8,0xf7,0x7f,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0xf8,
0x83,0x7f,0x0e,0x00,0x00,0x00,0x00,0x00,0xc0,0xfb,0x8f,0x7f,0x0e,0x00,0x00,
0x00,0x00,0x00,0xfc,0xfb,0xff,0x7f,0x0e,0x00,0x00,0x00,0x00,0x40,0xff,0xfb,
0xff,0x7f,0x0e,0x00,0x00,0x00,0x00,0xc0,0xfe,0xf9,0xff,0x7f,0x06,0x00,0x00,
0x00,0x00,0xc0,0xff,0xfd,0xff,0x7f,0x06,0x00,0x00,0x00,0x00,0x80,0xff,0xfc,
0xff,0x7f,0x06,0x00,0x00,0x00,0x00,0x80,0xff,0xfc,0xff,0x7f,0x07,0x00,0x00,
0x00,0x00,0x00,0x7f,0xfc,0xff,0xff,0x03,0x00,0x00,0x00,0x00,0x00,0x7f,0xfc,
0xff,0xff,0x03,0x00,0x00,0x00,0x00,0x00,0x7c,0xfc,0xff,0xff,0x03,0x00,0x00,
0x00,0x00,0x00,0x7c,0x10,0xff,0xff,0x01,0x00,0x00,0x00,0x00,0x00,0x7c,0x80,
0xff,0xff,0x01,0x00,0x00,0x00,0x00,0x00,0x3c,0xe0,0xff,0xff,0x00,0x00,0x00,
0x00,0x00,0x00,0x1e,0xfc,0xff,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x1e,0xfe,
0xff,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x0c,0xfc,0xff,0x1f,0x00,0x00,0x00,
0x00,0x00,0x00,0x0c,0x80,0xff,0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0x0c,0x80,
0xff,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x1c,0xff,0xff,0x07,0x00,0x00,0x00,
0x00,0x00,0x00,0x18,0xfe,0xff,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x18,0xc0,
0xff,0x03,0x00,0x00,0x00,0x00,0x00,0x40,0x30,0xc0,0xff,0x03,0x00,0x00,0x00,
0x00,0x00,0x40,0xe0,0xff,0xff,0x07,0x00,0x00,0x00,0x00,0x00,0x60,0xc0,0xff,
0x0f,0x07,0x00,0x00,0x00,0x00,0x00,0x60,0xc0,0xff,0x07,0x06,0x00,0x00,0x00,
0x00,0x00,0x60,0x80,0xff,0x03,0x0c,0x00,0x00,0x00,0x00,0x00,0x60,0x80,0xfe,
0x01,0x0c,0x00,0x00,0x00,0x00,0x00,0xe0,0x00,0x04,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0xe0,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x03,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x06,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0xc0,0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x3f,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0xff,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x80,0xff,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0xe3,0x07,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x81,0x0f,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x03,0x0e,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x03,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x03,0x00,0x00,0x00,0x00,0x00,0x00
};