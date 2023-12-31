﻿#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>

namespace Ui {
class Dialog;
}

class Dialog : public QDialog
{
   Q_OBJECT

public:
   explicit Dialog(QWidget *parent = 0);
   ~Dialog();

private slots:


   void on_btnClear_clicked();

    void on_chkBoxBold_toggled(bool checked);

   void on_chkBoxUnder_clicked();

    void on_chkBoxItalic_clicked(bool checked);

private:
   Ui::Dialog *ui;
};

#endif // DIALOG_H
