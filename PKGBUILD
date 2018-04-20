# Script generated with Bloom
pkgdesc="ROS - Launch files and world files to start the models in gazebo"
url='http://wiki.ros.org/summit_x_gazebo'

pkgname='ros-kinetic-summit-x-gazebo'
pkgver='1.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-gazebo-ros'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-summit-x-control'
'ros-kinetic-summit-x-description'
'ros-kinetic-summit-x-robot-control'
'ros-kinetic-tf'
'ros-kinetic-xacro'
)

depends=('ros-kinetic-gazebo-ros'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-summit-x-control'
'ros-kinetic-summit-x-description'
'ros-kinetic-summit-x-robot-control'
'ros-kinetic-tf'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=summit_x_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/summit_x_gazebo $srcdir/summit_x_gazebo
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

