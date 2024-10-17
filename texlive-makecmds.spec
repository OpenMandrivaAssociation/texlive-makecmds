Name:		texlive-makecmds
Version:	15878
Release:	2
Summary:	The new \makecommand command always (re)defines a command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makecmds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a \makecommand command, which is like
\(re)newcommand except it always (re)defines a command. There
is also \makeenvironment and \provideenvironment for
environments.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makecmds/makecmds.sty
%doc %{_texmfdistdir}/doc/latex/makecmds/README
%doc %{_texmfdistdir}/doc/latex/makecmds/makecmds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/makecmds/makecmds.dtx
%doc %{_texmfdistdir}/source/latex/makecmds/makecmds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
