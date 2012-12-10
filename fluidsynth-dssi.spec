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



%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 1.0.0-2
+ Revision: 793830
- rebuild, spec cleanup

* Fri Dec 04 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 473245
- new version 1.0.0
- fix license tag

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-4mdv2009.0
+ Revision: 245216
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.9.1-2mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import fluidsynth-dssi


* Mon Apr  3 2006 Austin Acton <austin@mandriva.org> 0.9.1-2mdk
- fix description

* Sat Apr  1 2006 Austin Acton <austin@mandriva.org> 0.9.1-1mdk
- adapt spec from Pedro Lopez-Cabanillas <plcl@users.sourceforge.net>
- initial package
