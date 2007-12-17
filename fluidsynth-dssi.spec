%define name	fluidsynth-dssi
%define version	0.9.1
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	DSSI plugin wrapper for the FluidSynth software synthesizer
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.bz2
URL:		http://dssi.sourceforge.net
License:	GPL
Group:		Sound
BuildRequires:	dssi-devel
BuildRequires:	liblo-devel
BuildRequires:	libalsa-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	gtk2-devel

%description
The FluidSynth-DSSI package contains FluidSynth-DSSI, a wrapper for the
FluidSynth SoundFont-playing software synthesizer, allowing it to function
as a DSSI plugin.

%prep
%setup -q

%build
alias libtoolize=true
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README TODO
%{_libdir}/dssi/%{name}/FluidSynth-DSSI_gtk
%{_libdir}/dssi/%{name}.la
%{_libdir}/dssi/%{name}.so
	       
