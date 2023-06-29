#include "Widget.h"
#include "ui_Widget.h"

Widget::Widget(QWidget *parent) :
   QWidget(parent),
   ui(new Ui::Widget)
{
   ui->setupUi(this);

}

Widget::~Widget()
{
   delete ui;
}


void Widget::on_slider_valueChanged(int value)
{

}


void Widget::on_radio_Percent_clicked()
{

}

