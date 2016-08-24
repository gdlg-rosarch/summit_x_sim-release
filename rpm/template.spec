Name:           ros-kinetic-summit-x-control
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS summit_x_control package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/RobotnikAutomation/summit_x_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-ros-control
Requires:       ros-kinetic-ros-controllers
Requires:       ros-kinetic-summit-x-description
Requires:       ros-kinetic-summit-xl-pad
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-robot-state-publisher
BuildRequires:  ros-kinetic-ros-control
BuildRequires:  ros-kinetic-ros-controllers
BuildRequires:  ros-kinetic-summit-x-description
BuildRequires:  ros-kinetic-summit-xl-pad

%description
This package contains the launch files that load the required controller
interfaces for simulation in Gazebo.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Aug 24 2016 Román Navarro <rnavarro@robotnik.es> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jul 19 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.6-0
- Autogenerated by Bloom

