﻿#include "Dialog.h"
#include "ui_Dialog.h"

Dialog::Dialog(QWidget *parent) :
   QDialog(parent),
   ui(new Ui::Dialog)
{
   ui->setupUi(this);
}

Dialog::~Dialog()
{
   delete ui;
}


void Dialog::on_btnClear_clicked()
{

}

void Dialog::on_chkBoxBold_toggled(bool checked)
{

}


void Dialog::on_chkBoxUnder_clicked()
{

}


void Dialog::on_chkBoxItalic_clicked(bool checked)
{

}

