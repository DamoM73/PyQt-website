# Tutorial 8 - Timer App UI

```{admonition} In this tutorial you will:
- stuff
```

To introduce more QT features we are going to make a new app, a clock/stopwatch/timer app.

To start this project we will create the UI file. Launch Qt Designer and create a new **Main Window**.

### Format the Main Window

For the **Main Window**:

1. Remove the **menu bar**
2. Remove the **status bar**
3. In the **Properties Editor**, change the **geometry** to:
   - **width** &rarr; **800**
   - **height** &rarr; **600**
4. Change the **windowTitle** to **Time Machine**

![main window setup](./assets/img/10/01_main_window_setup.gif)

### Add the Tab Widget

The **tab widget** is a container widget which is used to create multi-page UIs navigated using tabs.

```{admonition} Container Widgets
:class: hint
Qt **Container Widgets** are special widgets that hold and organize other widgets inside them. They help structure a GUI by grouping buttons, labels, and other elements neatly.

Common Container Widgets:

1. **[QWidget](https://doc.qt.io/qt-6/qwidget.html)** – The basic container for any widgets.
2. **[QGroupBox](https://doc.qt.io/qt-6/qgroupbox.html)** – A box with a title, used to group related widgets.
3. **[QFrame](https://doc.qt.io/qt-6/qframe.html)** – A simple container with a border.
4. **[QTabWidget](https://doc.qt.io/qt-6/qtabwidget.html)** – Creates a tabbed interface.
5. **[QStackedWidget](https://doc.qt.io/qt-6/qstackedwidget.html)** – Lets you switch between different screens (like pages).
6. **[QScrollArea](https://doc.qt.io/qt-6/qscrollarea.html)** – Adds scrollbars when content is too big.
7. **[QSplitter](https://doc.qt.io/qt-6/qsplitter.html)** – Allows resizing of sections by dragging.
```

1. In the **Containers** section of the **Widgets Toolbox** find the **Tab Widget**.
2. Click and drag it onto the **window canvas**
3. Then right-click the **window canvas**, choose **Layout** then **Lay Out Vertically**

![add tabs](./assets/img/10/02_add_tabs.gif)

### Organise the tabs

We will three tabs - **Time**, **Stopwatch** and **Timer**, so we need to add a tab.

1. Go to the **Object Inspector**
2. Right-click on the **tabWidget**
3. Choose **Insert Page** &rarr; **After Current Page**

![insert tab](./assets/img/10/03_insert_tab.gif)

Now we need to name the tabs

4. Click on the **left tab**
5. The the **Property Editor** scroll down to the QTabWidget section
6. Change **currentTabText** &rarr; **Clock**
7. Change **currentTabName** &rarr; **tab_clock**
8. Click on the **centre tab**
9. Change **currentTabText** &rarr; **Stopwatch**
10. Change **currentTabName** &rarr; **tab_stopwatch**
11. Click on the **right tab**
12. Change **currentTabText** &rarr; **Timer**
13. Change **currentTabName** &rarr; **tab_timer**

![name tabs](./assets/img/10/04_naming_tabs.gif)

To make the tabs easier to read, resize the font

14. Click on the **Clock** tab and change the **font Point Size** to **20**

![font size](./assets/img/10/05_font_size.gif)

### Populate the Clock tab

Now to add the required elements onto the Clock tab.

1. Click on the **Clock** tab
2. Drag the **Label Widget** from the **Widgets Toolbox** to the **windows canvas**
3. Then right-click the **window canvas**, choose **Layout** then **Lay Out Vertically**
4. At the top of the **Properties Editor**, find **objectName**
5. Change it to **label_clock**

![add clock label](./assets/img/10/06_add_clcok_label.gif)

Now to format the **clock_label**

6. Change the **font Point Size** to 100
7. Then scroll down and find **alignment Horizontal** and change it to **AlignHCenter**

![format clock](./assets/img/10/07_format_clock.gif)

### Populate the Stopwatch tab

On to adding elements to the Stopwatch tab.

1. Click on the **Stopwatch** tab
2. Drag the **Label Widget** from the **Widgets Toolbox** to the top half of the **windows canvas**
3. Locate and drag the **Horizontal Layout** to the bottom half of the **windows canvas**
4. Then right-click the **window canvas**, choose **Layout** then **Lay Out Vertically**

![add stopwatch label](./assets/img/10/08_add_stopwatch_label.gif)

5. Drag four **Push Buttons** into the **Horizontal Layout**
6. Drag a **Vertical Space** above and below the **Label**

![stopwatch layout](./assets/img/10/09_stopwatch_layout.gif)

7. Change the Label name &rarr; **label_stopwatch**
8. Change the first Push Button name &rarr; **pushButton_sw_start**
9. Change the first Push Button text &rarr; **Start**
10. Change the second Push Button name to &rarr; **pushButton_sw_pause**
11. Change the second Push Button text &rarr; **Pause**
12. Change the third Push Button name to &rarr; **pushButton_sw_stop**
13. Change the third Push Button text &rarr; **Stop**
14. Change the forth Push Button name to &rarr; **pushButton_sw_reset**
15. Change the forth Push Button text &rarr; **Reset**
 
![stopwatch names](./assets/img/10/10_stopwatch_names.gif)

16. Change the **label_stopwatch font Point Size** &rarr; 100
17. Then scroll down and find **alignment Horizontal** and change it to **AlignHCenter**
18. Change the **font Point Size** of all the Push Buttons &rarr; 30

![stopwatch format](./assets/img/10/11_stop_watch_format.gif)

19. Find the **sizePolicy** and change the **Vertical Policy** to **MinimumExpanding** for **label_stopwatch** and all the Push Buttons.

![set size policy](./assets/img/10/12_stopwatch_size_policy.gif)

### Populate the Timer tab

1. Click on the **Stopwatch** tab
2. Drag the **Label Widget** from the **Widgets Toolbox** to the top half of the **windows canvas**
3. Locate the **Grid Layout** and drag it to under the **Label Widget**
4. Locate the **Horizontal Layout** and drag it under the **Grid Layout**
5. Then right-click the **window canvas**, choose **Layout** then **Lay Out Vertically**

![adding label to timer](./assets/img/10/13_add_timer_label.gif)

6. Drag three **Labels** side-by-side in the **Grid Layout**
7. Change the first label:
   - text &rarr; **Hours**
   - horizontal alignment &rarr; **AlignVCenter**
8. Change the second label: 
   - text &rarr; **Minutes**
   - horizontal alignment &rarr; **AlignVCenter**
9.  Change the third label:
    - text &rarr; **Seconds**
    - horizontal alignment &rarr; **AlignVCenter**

![Spin box labels](./assets/img/10/14__timer_spin_labels.gif)

10. Add a spinbox under each of the labels
11. Name the first spinbox &rarr; **spinBox_hours**
12. Name the second spinbox &rarr; **spinBox_minutes**
13. Name the third spinbox &rarr; **spinBox_seconds**

![add spinboxes](./assets/img/10/15__timer_spin_boxes.gif)

14. For each spinbox:
    - change font **Point Size** &rarr; **30**
    - change **Horizontal** alignment &rarr; **AlignRight**

![format spin boxes](./assets/img/10/16_format_spin_boxes.gif)

15. Drag four **Push Buttons** into the **Horizontal Layout**

![add timer buttons](./assets/img/10/17_add_timer_buttons.gif)

16. For the first button:
    - text &rarr; **Start**
    - font **Point Size** &rarr; **30**
17. For the first button:
    - text &rarr; **Stop**
    - font **Point Size** &rarr; **30**
18. For the first button:
    - text &rarr; **Pause**
    - font **Point Size** &rarr; **30**
19. For the first button:
    - text &rarr; **Reset**
    - font **Point Size** &rarr; **30**

![format timer buttons](./assets/img/10/18_format_timer_buttons.gif)

20. Name the start button &rarr; **pushButton_tm_start**
21. Name the stop button &rarr; **pushButton_tm_stop**
22. Name the pause button &rarr; **pushButton_tm_pause**
23. Name the reset button &rarr; **pushButton_tm_reset**

![format timer buttons](./assets/img/10/18_format_timer_buttons.gif)

24. Change the name of the top table &rarr; **label_tm_time**
25. Change font **Point Size** &rarr; **100**
26. Change the **Horizontal** alignment &rarr; **AlignHCenter**
27. Add a **Vertical Spacer** above and below the label

![format timer time label](./assets/img/10/19_format_timer_time_label.gif)

That the UI done. Make sure you save before testing.

## Testing

Time to make sure that everything is working as we designed.

Launch the preview with Ctrl-R

Check all the tabs, buttons and spinboxes. They won't do muck yet, but make sure that they are there.