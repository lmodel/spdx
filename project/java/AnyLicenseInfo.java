package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Abstract class representing a license combination consisting of one or more licenses.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AnyLicenseInfo extends Element {



}