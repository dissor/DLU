import QtQuick 2.0
import QtQuick.Controls 2.1

ApplicationWindow {
    id: page
    width: 800
    height: 400
    visible: true

    Rectangle {
        id: main
        width: 200
        height: 200
        color: "green"
        opacity: 0.5

        Text {
            text: "Hello World"
            anchors.centerIn: main
        }
    }
}
