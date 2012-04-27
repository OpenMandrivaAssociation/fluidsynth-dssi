Name:       fluidsynth-dssi
Summary:    DSSI plugin wrapper for the FluidSynth software synthesizer
Version:    1.0.0
Release:    2

Source:     http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
URL:        http://dssi.sourceforge.net
License:    GPLv2+
Group:      Sound

BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(fluidsynth)

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

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README TODO
%{_libdir}/dssi/%{name}/FluidSynth-DSSI_gtk
%{_libdir}/dssi/%{name}.so

