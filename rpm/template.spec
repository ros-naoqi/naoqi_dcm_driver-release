Name:           ros-kinetic-naoqi-dcm-driver
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS naoqi_dcm_driver package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-naoqi-libqi
Requires:       ros-kinetic-naoqi-libqicore
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-naoqi-libqi
BuildRequires:  ros-kinetic-naoqi-libqicore
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
Package containing the hardware interface to connect to Nao, Romeo, or Pepper
robots.

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
* Thu Nov 16 2017 Natalia Lyubova <natalia.lyubova@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Tue Sep 20 2016 Natalia Lyubova <natalia.lyubova@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Sun Sep 18 2016 Natalia Lyubova <natalia.lyubova@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

