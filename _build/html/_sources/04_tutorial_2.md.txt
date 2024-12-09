# Tutorial 2 - Labels

```{admonition} In this tutorial you will learn to:
- chagne label geometry
- change label alignment
- change label margins
- copy widhets in a window
- use labels to add images
- change label font colour
- change label back-ground colour
- change label boarders
```

Label widgets are Qt's the most commonly used display widget. The majority of your UI will be made up of labels. In this tutorial you will learn how to change some of the basic label properties.

```{admonition} Qt Documentation
:class: seealso
For additional information about labels, check the official **[QLabel documentaion](https://doc.qt.io/qt-6/qlabel.html)** from Qt.
```

## Create new window

Using your knowledge from the last tutorial:

1. Create a new **MainWindow**
2. Remove the **menu bar**
3. Change the **windowTitle** to **Tutorial 2**

## First label

We need to add a new label.

1. Scroll down the **Widget library** until you find **Label**
2. Click and drag a **Label** to the centre of the **window canvas**
3. Double Click on the label and change the text to **Hello World**

![add label 1](./assets/img/04/01_label_1.gif)

Now we need to adjust the geometry and font size.

4. Click on the label to select it, then in the **Properties editor** locate the label's **geometry**
5. Change the **width** to **260** and the **height** to **120**
6. Change the **font** **Point Size** to **20**

![edit label 1 geometry](./assets/img/04/02_label_1.gif)

Next we will change the alignment of the text inside the label.

7. Scroll down further in the **Properties editor** until you find the **QLabel** section.
8. Locate the **alignment** section and click the **>** beside it, which should reveal the **Horizontal** and **Vertical** properties.
9.  Click on the **Vertical** options and choose **AlignTop**
10. Change the **Margin** to **20**

![change alignment](./assets/img/04/03_label_1.gif)

Finally we will format the label using its style sheet.

11. Scroll back up to the **QWidget** sections and find **styleSheet**
12. Click on the ellipses (**...**) on the righthand side
13. Type **background-color: red;** to change the label background colour to red
14. Type **color: yellow** to change the font colour to yellow
15. Type **border: 2px solid black;** to put a black border around the label
16. Check that the style sheet is **valid** then click **OK**

![change style sheet](./assets/img/04/04_label_1.gif)

```{admonition} Style Sheets
:class: hint
Style sheets in Qt are a power mechanism that allows you to change the appearance of individual widgets, or the entire application. We will be using style sheets in later tutiorials, but you can explore Qt Style Sheets using their **[documenation](https://doc.qt.io/qt-6/stylesheet.html)**.
```

## Second label

To make the second label, we will simply copy the first one.

1. Copy the first widget by holding the **Ctrl** / **Cmd** key whilst clicking and dragging the first widget.
2. Double Click on the label and change the text to **It is me**

![label 2 copy](./assets/img/04/05_label_2.gif)

We will change the alignment of the second label.

3. Locate the **alignment** section and click the **>** beside it, which should reveal the **Horizontal** and **Vertical** properties.
4. Click on the **Horizontal** options and choose **AlignHCenter**
5. Click on the **Vertical** options and choose **AlignVCenter**

![label 2 alignment](./assets/img/04/06_label_2.gif)

We will also change the style of label 2 so it differs from label 1.

6. Open its style sheet
7. Delete **color: yellow**
9. Delete **border: 2px solid black;**
10. Change to  **background-color: cyan;**
11. Check that the style sheet is **valid** then click **OK**

![label 2 style](./assets/img/04/07_label_2.gif)

## Third label

Label can contain more than text, they can also contain images. For the third label you will need to use the image below. **Right-click** on it and **save** it to you repo.

![mr-coder](./assets/img/04/mr-coder.png)  

Add a new label to the window canvas above the other labels.

1. Scroll down the **Widget library** until you find **Label**
2. Click and drag a **Label** to the centre of the **window canvas**

![add label 3](./assets/img/04/08_label_3.gif)

Now to add the image.

3. Scroll down the **Properties editor** until you find the **QLabel** section
4. Find **pixmap** and click on the empty space to the right of it
5. Click on dropdown arrow that appears and then click **Choose File...**
6. Navigate to, and select the **mr-coder.png** image you just saved (note, your location will be different to the location shown in the gif)
7. Then tick the checkbox beside **scaledContent**

![add image](./assets/img/04/09_label_3.gif)

We need to change the label geometry so we can see the image.

8. Scroll back up to the **QWidget** section and adjust the label's **geometry**.
9.  **width** to **250**
10. **height** to **70**

![change label 3 geometry](./assets/img/04/10_label_3.gif)

## Create Python UI file

### Save the UI file

Time to save the UI. It is important to save the UI file in the same directory (folder) as your **main_window.py**, ie. your repo for these tutorials.

1. Select **Save** from the **File** menu
2. Navigate to your repo with your **main_window.py** file
3. Name the file **tutorial_02.ui**

### Convert UI file

Now we need to convert the UI file to a Python file, and we will do this in VS Code.

1. Open VS Code via GitHub Desktop
2. Check that the **tutorial_02.ui** file is in your file panel.
3. Open a new terminal
4. At the prompt, type `pyuic6 -o ui_main_window.py -x tutorial_02.ui`
5. Then press enter.

Time to run the app and check that it all works

6. Open the **main_window.py**
7. Run the code.

A window similar to the one below should appear.

![finished window](./assets/img/04/finished_window.png)

## Conclusion

In this tutorial we covered changing some to the basic functions of the QLabel widget. There are many, many more properties, but these should be sufficient to create most UIs. If you want to explore more options check out the Qt documentation.