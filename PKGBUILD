# Script generated with Bloom
pkgdesc="ROS - This package contains the launch files that load the required controller interfaces for simulation in Gazebo."
url='https://github.com/RobotnikAutomation/summit_x_control'

pkgname='ros-kinetic-summit-x-control'
pkgver='1.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-ros-control'
'ros-kinetic-ros-controllers'
'ros-kinetic-summit-x-description'
'ros-kinetic-summit-xl-pad'
)

depends=('ros-kinetic-robot-state-publisher'
'ros-kinetic-ros-control'
'ros-kinetic-ros-controllers'
'ros-kinetic-summit-x-description'
'ros-kinetic-summit-xl-pad'
)

conflicts=()
replaces=()

_dir=summit_x_control
source=()
md5sums=()

prepare() {
    cp -R $startdir/summit_x_control $srcdir/summit_x_control
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

